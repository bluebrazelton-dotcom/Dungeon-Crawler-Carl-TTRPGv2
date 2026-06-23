"""
DCC v2 Chaos Engine — Chaos Clock (Hybrid Mode)
Pre-rolls TIMING before the session. Doug rolls EVENT live when clock fires.

Workflow:
  1. Session prep: run `pre_roll_schedule` → prints a list of fire times.
  2. During play: when a fire time hits, Doug rolls → narrator looks up result.
"""

import random
from roller_core import load_floor_tables, weighted_pick, format_player_roll, format_narrator_result


def pre_roll_schedule(floor_number: int, session_length_minutes: int = 180) -> list[int]:
    """
    Generate a sequence of chaos clock fire times for a session.
    Returns list of minute marks (e.g., [23, 51, 82, 114]).
    """
    tables = load_floor_tables(floor_number)
    clock = tables.get("chaos_clock", {})
    min_interval = clock.get("min_interval_minutes", 20)
    max_interval = clock.get("max_interval_minutes", 40)

    times = []
    current = random.randint(min_interval, max_interval)
    while current <= session_length_minutes:
        times.append(current)
        current += random.randint(min_interval, max_interval)

    return times


def roll_clock_event(floor_number: int, fired_events: list[int] | None = None) -> dict:
    """
    Roll a chaos clock event. Doug calls this live when the clock fires.
    fired_events: list of event IDs already fired this session (for one_shot filtering).
    Returns dict with 'player_view' and 'narrator_view'.
    """
    fired_events = fired_events or []
    tables = load_floor_tables(floor_number)
    clock = tables.get("chaos_clock", {})
    events = clock.get("events", [])

    # Filter out one-shot events that already fired
    available = [e for e in events if not (e.get("one_shot", False) and e["id"] in fired_events)]

    if not available:
        return {
            "player_view": "[Chaos Clock] Roll: -- (pool exhausted, no event)",
            "narrator_view": "[Chaos Clock] NARRATOR ONLY\n  All one-shot events spent. Clock fires but nothing happens.",
            "entry": None,
        }

    result = weighted_pick(available)

    return {
        "player_view": format_player_roll(result["id"], len(available), "Chaos Clock"),
        "narrator_view": format_narrator_result(result, "Chaos Clock"),
        "entry": result,
    }


if __name__ == "__main__":
    import sys
    floor = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    mode = sys.argv[2] if len(sys.argv) > 2 else "schedule"
    session_len = int(sys.argv[3]) if len(sys.argv) > 3 else 180

    if mode == "schedule":
        times = pre_roll_schedule(floor, session_len)
        print(f"Chaos Clock schedule for Floor {floor} ({session_len} min session):")
        print(f"  Fire times: {', '.join(f'{t} min' for t in times)}")
        print(f"  Total fires: {len(times)}")
        print()
        print("When each time hits, run: python chaos_clock.py <floor> event")
    elif mode == "event":
        result = roll_clock_event(floor)
        print(result["player_view"])
        print()
        print(result["narrator_view"])
    else:
        print(f"Usage: python chaos_clock.py <floor> [schedule|event] [session_minutes]")
