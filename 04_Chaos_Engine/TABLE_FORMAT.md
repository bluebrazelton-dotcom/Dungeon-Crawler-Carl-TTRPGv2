# Chaos Engine — Table Format Guide

Reference for populating floor tables during Build Sessions.

## File Naming

Each floor gets one JSON file: `floor_01_tables.json`, `floor_02_tables.json`, etc.
Copy `floor_XX_tables.json.example` as your starting template.

## Structure Overview

A floor table file has five top-level keys:

```
_meta              → Floor metadata (name, date, notes)
event_tables       → Triggered events (5 trigger types)
chaos_clock        → Timed dungeon-wide events
loot_tables        → Items by tier + zone overrides
encounter_modifiers → Combat modifications
```

## Event Tables

**Trigger types:** `enter_area`, `rest`, `kill_enemy`, `linger`, `open_loot`

Each trigger has a list of entries. Per the blueprint: 12-20 entries per trigger, including 3-4 genuinely inconvenient results and 2-3 absurdly funny ones.

```json
{
  "id": 1,
  "weight": 3,
  "result": "Description of what happens. Be specific enough that the narrator can integrate it without inventing details.",
  "tags": ["hazard", "dex"]
}
```

**Fields:**
- `id` (int): Unique within this trigger table. Sequential.
- `weight` (int): Higher = more likely. Use 1 for rare, 2-3 for common, 4+ for very frequent.
- `result` (string): The full event description. Narrator-only. Write as if briefing the narrator: what happens, what check (if any), what consequence.
- `tags` (list[str]): Freeform. Useful for narrator context. Common: `neutral`, `hazard`, `combat`, `loot`, `fame`, `funny`, `choice`, `urgent`, `dex`, `str`, `int`, etc.

**Weight guidelines for a 15-entry table:**
- 5-6 entries at weight 3 (common, ~50% of rolls)
- 4-5 entries at weight 2 (uncommon, ~30%)
- 3-4 entries at weight 1 (rare, ~15%)
- 1-2 entries at weight 1 (the chaos/funny ones)

## Chaos Clock

```json
{
  "min_interval_minutes": 20,
  "max_interval_minutes": 40,
  "events": [...]
}
```

Per blueprint: 20-30 events per floor. Includes sponsor interventions, rule changes, competitions, environmental shifts.

Event entries:
```json
{
  "id": 1,
  "weight": 2,
  "result": "SPONSOR ALERT: ...",
  "tags": ["sponsor", "choice"],
  "one_shot": false
}
```

- `one_shot` (bool): If true, this event can only fire once per session. Use for dramatic events that lose impact on repeat. The engine tracks fired one-shots automatically.

**Timing:** The engine pre-rolls fire times (hybrid mode). Doug rolls the event live when the clock hits. Intervals are randomized between min and max.

## Loot Tables

Two-stage roll: pick a tier, then pick an item from that tier.

```json
"tiers": {
  "common":    {"weight": 50, "items": [...]},
  "uncommon":  {"weight": 30, "items": [...]},
  "rare":      {"weight": 12, "items": [...]},
  "legendary": {"weight": 5,  "items": [...]},
  "chaos":     {"weight": 3,  "items": [...]}
}
```

**Tier weights** are the probability distribution. The example above gives chaos loot a ~3% chance (within the blueprint's 10-15% chaos band when you factor in legendary oddities). Adjust per floor.

Item entries:
```json
{
  "id": 1,
  "name": "Item Name",
  "description": "What it does. Include mechanical effects.",
  "tags": ["weapon", "melee", "fire"],
  "value": 150
}
```

- `tags`: Used for the tag synergy system (2 matching = +1, 3 = +3 + passive, 4+ = +5 + major). Tag items deliberately to create synergy possibilities.
- `value`: In-game currency value. Used for shop pricing and sell value.
- Items within a tier are equally weighted by default. Add a `"weight"` field to an item to make it more/less common within its tier.

**Zones** allow area-specific loot behavior:
```json
"zones": {
  "zone_a": {
    "name": "Starting Zone",
    "tier_override": null,
    "bonus_items": []
  },
  "boss_zone": {
    "name": "Boss Chamber",
    "tier_override": {"legendary": 10, "chaos": 5},
    "bonus_items": [{"id": 1, "name": "Boss Trophy", ...}]
  }
}
```

- `tier_override`: Replaces specific tier weights for this zone. Others stay at default.
- `bonus_items`: Extra items that can drop in addition to the main roll. Only in this zone.

## Encounter Modifiers

```json
{
  "trigger_chance_percent": 50,
  "modifiers": [...]
}
```

Per blueprint: 40-60% trigger chance, 10-15 modifiers per floor.

Modifier entries use the same format as event table entries (id, weight, result, tags).

**Design note:** Modifiers should be environment-aware but not encounter-specific. "Reinforcements arrive" works everywhere. "The dragon's nest catches fire" is too specific. Let the narrator contextualize.

## Checklist for a Complete Floor

- [ ] `_meta` filled in (floor number, name, date)
- [ ] 5 event tables, each with 12-20 entries
- [ ] Weight distribution includes inconvenient (3-4) and funny (2-3) entries per table
- [ ] Chaos clock with 20-30 events
- [ ] At least 3-5 one-shot events in the clock pool
- [ ] Loot tiers with 8-15 items each (more at common, fewer at chaos)
- [ ] Chaos tier includes 3-5 wildly off-theme items
- [ ] Zones defined matching the floor map
- [ ] 10-15 encounter modifiers
- [ ] All items have tags that create deliberate synergy opportunities
- [ ] No result contradicts established game rules (death on Floors 1-3, etc.)
