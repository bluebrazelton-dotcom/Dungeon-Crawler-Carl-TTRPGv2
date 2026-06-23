"""
DCC v2 Chaos Engine — Loot Roller
Probability-distributed loot by tier. 10-15% chaos loot chance built into tier weights.
Zones can override tier weights for boss areas, shops, etc.
"""

from roller_core import load_floor_tables, weighted_pick, format_player_roll, format_narrator_result


def roll_loot(floor_number: int, zone: str | None = None) -> dict:
    """
    Roll for loot on the given floor, optionally in a specific zone.
    Two-stage roll: pick tier, then pick item within tier.
    Returns dict with 'player_view', 'narrator_view', and 'entry'.
    """
    tables = load_floor_tables(floor_number)
    loot = tables.get("loot_tables", {})
    tiers = loot.get("tiers", {})
    zones = loot.get("zones", {})

    if not tiers:
        raise ValueError(f"No loot tiers defined for Floor {floor_number}.")

    # Check for zone-specific tier overrides
    tier_weights = {name: data["weight"] for name, data in tiers.items()}
    zone_name = None
    if zone and zone in zones:
        zone_data = zones[zone]
        zone_name = zone_data.get("name", zone)
        overrides = zone_data.get("tier_override")
        if overrides:
            tier_weights.update(overrides)

    # Stage 1: Pick a tier
    tier_entries = [{"name": name, "weight": weight} for name, weight in tier_weights.items()]
    chosen_tier = weighted_pick(tier_entries)
    tier_name = chosen_tier["name"]

    # Stage 2: Pick an item from that tier
    items = tiers[tier_name]["items"]
    if not items:
        return {
            "player_view": f"[Loot] Tier: {tier_name} — but the table is empty. Nothing drops.",
            "narrator_view": f"[Loot] NARRATOR ONLY\n  Tier '{tier_name}' has no items for Floor {floor_number}.",
            "entry": None,
        }

    item = weighted_pick([{**i, "weight": i.get("weight", 1)} for i in items])

    # Zone bonus items
    bonus = None
    if zone and zone in zones:
        bonus_items = zones[zone].get("bonus_items", [])
        if bonus_items:
            bonus = weighted_pick([{**i, "weight": i.get("weight", 1)} for i in bonus_items])

    # Format output
    player_line = f"[Loot] Tier roll: {tier_name.upper()} | Item roll: #{item['id']} (of {len(items)})"
    if zone_name:
        player_line += f" | Zone: {zone_name}"

    tags = ", ".join(item.get("tags", []))
    narrator_lines = [
        f"[Loot] NARRATOR ONLY",
        f"  Tier: {tier_name}",
        f"  Item: {item['name']}",
        f"  Description: {item['description']}",
        f"  Tags: {tags}",
        f"  Value: {item.get('value', '???')}",
    ]
    if bonus:
        narrator_lines.append(f"  BONUS (zone): {bonus['name']} — {bonus['description']}")

    return {
        "player_view": player_line,
        "narrator_view": "\n".join(narrator_lines),
        "entry": item,
        "tier": tier_name,
        "bonus": bonus,
    }


def list_zones(floor_number: int) -> list[str]:
    """List available zones for a floor."""
    tables = load_floor_tables(floor_number)
    zones = tables.get("loot_tables", {}).get("zones", {})
    return [f"{k}: {v.get('name', k)}" for k, v in zones.items()]


if __name__ == "__main__":
    import sys
    floor = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    zone = sys.argv[2] if len(sys.argv) > 2 else None

    if zone == "zones":
        available = list_zones(floor)
        print(f"Floor {floor} zones:")
        for z in available:
            print(f"  {z}")
    else:
        result = roll_loot(floor, zone)
        print(result["player_view"])
        print()
        print(result["narrator_view"])
