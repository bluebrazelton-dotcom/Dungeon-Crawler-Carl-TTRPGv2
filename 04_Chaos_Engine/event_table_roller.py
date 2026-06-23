"""
DCC v2 Chaos Engine — Event Table Roller
Triggered by player actions: enter_area, rest, kill_enemy, linger, open_loot.
Doug rolls → sees a number. Narrator sees the result.
"""

from roller_core import load_floor_tables, weighted_pick, format_player_roll, format_narrator_result

VALID_TRIGGERS = ["enter_area", "rest", "kill_enemy", "linger", "open_loot"]


def roll_event(floor_number: int, trigger: str) -> dict:
    """
    Roll on an event table for the given trigger type.
    Returns dict with 'player_view' and 'narrator_view' strings.
    """
    if trigger not in VALID_TRIGGERS:
        raise ValueError(f"Invalid trigger '{trigger}'. Valid: {VALID_TRIGGERS}")

    tables = load_floor_tables(floor_number)
    event_tables = tables.get("event_tables", {})

    if trigger not in event_tables:
        raise ValueError(f"No event table for trigger '{trigger}' on Floor {floor_number}.")

    entries = event_tables[trigger]
    result = weighted_pick(entries)

    return {
        "trigger": trigger,
        "player_view": format_player_roll(result["id"], len(entries), f"Event:{trigger}"),
        "narrator_view": format_narrator_result(result, f"Event:{trigger}"),
        "entry": result,
    }


def list_triggers(floor_number: int) -> list[str]:
    """List available trigger types for a floor."""
    tables = load_floor_tables(floor_number)
    return list(tables.get("event_tables", {}).keys())


if __name__ == "__main__":
    import sys
    floor = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    trigger = sys.argv[2] if len(sys.argv) > 2 else None

    if trigger is None:
        available = list_triggers(floor)
        print(f"Floor {floor} triggers: {', '.join(available)}")
        print(f"Usage: python event_table_roller.py {floor} <trigger>")
    else:
        result = roll_event(floor, trigger)
        print(result["player_view"])
        print()
        print(result["narrator_view"])
