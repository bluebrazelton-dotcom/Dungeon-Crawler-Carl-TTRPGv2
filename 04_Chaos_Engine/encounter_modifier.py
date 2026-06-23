"""
DCC v2 Chaos Engine — Encounter Modifier
40-60% chance per encounter of modification.
Two-stage: roll to see IF a modifier fires, then roll WHICH one.
"""

import random
from roller_core import load_floor_tables, weighted_pick, format_player_roll, format_narrator_result


def roll_encounter_modifier(floor_number: int) -> dict:
    """
    Roll for encounter modification.
    Returns dict with 'modified' bool, 'player_view', 'narrator_view', 'entry'.
    """
    tables = load_floor_tables(floor_number)
    enc = tables.get("encounter_modifiers", {})
    trigger_chance = enc.get("trigger_chance_percent", 50)
    modifiers = enc.get("modifiers", [])

    # Stage 1: Does a modifier fire?
    trigger_roll = random.randint(1, 100)
    fires = trigger_roll <= trigger_chance

    if not fires:
        return {
            "modified": False,
            "player_view": f"[Encounter Mod] Trigger roll: {trigger_roll} (need ≤{trigger_chance}) — NO MODIFIER",
            "narrator_view": f"[Encounter Mod] No modification. Clean encounter.",
            "entry": None,
        }

    if not modifiers:
        return {
            "modified": False,
            "player_view": f"[Encounter Mod] Trigger roll: {trigger_roll} — modifier triggered but table empty.",
            "narrator_view": f"[Encounter Mod] NARRATOR ONLY\n  Modifier triggered but no modifiers defined for Floor {floor_number}.",
            "entry": None,
        }

    # Stage 2: Which modifier?
    result = weighted_pick(modifiers)

    return {
        "modified": True,
        "player_view": f"[Encounter Mod] Trigger roll: {trigger_roll} (need ≤{trigger_chance}) — MODIFIER ACTIVE | Roll: #{result['id']} (of {len(modifiers)})",
        "narrator_view": format_narrator_result(result, "Encounter Mod"),
        "entry": result,
    }


if __name__ == "__main__":
    import sys
    floor = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    result = roll_encounter_modifier(floor)
    print(result["player_view"])
    print()
    print(result["narrator_view"])
