"""
DCC v2 Chaos Engine — Master Interface
Single entry point for all rollers. Two modes:
  - Interactive CLI (menu-driven during play)
  - Session prep (pre-roll chaos clock schedule)

Usage:
  python chaos_engine.py <floor>           → Interactive mode
  python chaos_engine.py <floor> prep      → Session prep (clock schedule)
  python chaos_engine.py <floor> prep 240  → Session prep (custom length in minutes)
"""

import sys
from roller_core import divider

from event_table_roller import roll_event, list_triggers
from chaos_clock import pre_roll_schedule, roll_clock_event
from loot_roller import roll_loot, list_zones
from encounter_modifier import roll_encounter_modifier


def session_prep(floor: int, session_minutes: int = 180):
    """Pre-session prep: generate chaos clock schedule."""
    print(divider("SESSION PREP"))
    print(f"  Floor: {floor}")
    print(f"  Session length: {session_minutes} minutes")
    print()

    # Chaos clock schedule
    times = pre_roll_schedule(floor, session_minutes)
    print("  CHAOS CLOCK FIRE TIMES:")
    for i, t in enumerate(times, 1):
        h, m = divmod(t, 60)
        timestamp = f"{h}h{m:02d}m" if h else f"{m}m"
        print(f"    #{i}: {timestamp} into session")
    print(f"\n  Total clock fires: {len(times)}")
    print(f"  When each fires, select 'Chaos Clock Event' from the menu.")
    print(divider())


def interactive(floor: int):
    """Interactive menu for live play."""
    fired_clock_events: list[int] = []

    print(divider(f"CHAOS ENGINE — FLOOR {floor}"))
    print("  All rolls show TWO outputs:")
    print("  • PLAYER VIEW: What Doug sees (numbers only)")
    print("  • NARRATOR VIEW: What the narrator integrates (full result)")
    print(divider())

    while True:
        print("\n  ROLLERS:")
        print("  [1] Event Table      (trigger-based)")
        print("  [2] Chaos Clock Event (when timer fires)")
        print("  [3] Loot Roller      (loot drop)")
        print("  [4] Encounter Modifier (before combat)")
        print("  [5] Session Prep     (pre-roll clock schedule)")
        print("  [q] Quit")

        choice = input("\n  > ").strip().lower()

        if choice == "q":
            print("\n  Engine shutting down. The dungeon remembers.\n")
            break

        elif choice == "1":
            triggers = list_triggers(floor)
            print(f"\n  Available triggers: {', '.join(triggers)}")
            trigger = input("  Which trigger? > ").strip().lower()
            try:
                result = roll_event(floor, trigger)
                print(f"\n  — PLAYER VIEW —\n  {result['player_view']}")
                print(f"\n  — NARRATOR VIEW —\n  {result['narrator_view']}")
            except (ValueError, KeyError) as e:
                print(f"\n  Error: {e}")

        elif choice == "2":
            result = roll_clock_event(floor, fired_clock_events)
            print(f"\n  — PLAYER VIEW —\n  {result['player_view']}")
            print(f"\n  — NARRATOR VIEW —\n  {result['narrator_view']}")
            if result["entry"] and result["entry"].get("one_shot"):
                fired_clock_events.append(result["entry"]["id"])

        elif choice == "3":
            zones = list_zones(floor)
            if zones:
                print(f"\n  Available zones:")
                for z in zones:
                    print(f"    {z}")
                zone = input("  Zone (or Enter for general): > ").strip().lower() or None
            else:
                zone = None
            result = roll_loot(floor, zone)
            print(f"\n  — PLAYER VIEW —\n  {result['player_view']}")
            print(f"\n  — NARRATOR VIEW —\n  {result['narrator_view']}")

        elif choice == "4":
            result = roll_encounter_modifier(floor)
            print(f"\n  — PLAYER VIEW —\n  {result['player_view']}")
            print(f"\n  — NARRATOR VIEW —\n  {result['narrator_view']}")

        elif choice == "5":
            length = input("  Session length in minutes [180]: > ").strip()
            length = int(length) if length else 180
            session_prep(floor, length)

        else:
            print("  Invalid choice.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python chaos_engine.py <floor> [prep] [session_minutes]")
        print("  <floor>          Floor number (e.g., 1)")
        print("  prep             Pre-roll chaos clock schedule")
        print("  session_minutes  Session length for prep mode (default: 180)")
        sys.exit(1)

    floor = int(sys.argv[1])
    mode = sys.argv[2] if len(sys.argv) > 2 else "interactive"

    if mode == "prep":
        session_minutes = int(sys.argv[3]) if len(sys.argv) > 3 else 180
        session_prep(floor, session_minutes)
    else:
        interactive(floor)


if __name__ == "__main__":
    main()
