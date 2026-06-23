"""
DCC v2 — Snapshot Status Tool
Lists all snapshots and rollback history. Quick audit for campaign state.

Usage:
  python snapshot_status.py           → List all snapshots
  python snapshot_status.py --detail  → Include file lists
  python snapshot_status.py --history → Show rollback history
"""

import argparse
import json
from pathlib import Path

ENGINE_DIR = Path(__file__).parent
DCC_V2_DIR = ENGINE_DIR.parent
SNAPSHOTS_DIR = DCC_V2_DIR / "05_Snapshots"
ROLLBACK_LOG = SNAPSHOTS_DIR / "rollback_history.json"


def list_snapshots(detail: bool = False):
    """List all snapshots with manifest summaries."""
    if not SNAPSHOTS_DIR.exists():
        print("No 05_Snapshots/ directory found. No snapshots taken yet.")
        return

    dirs = sorted([
        d for d in SNAPSHOTS_DIR.iterdir()
        if d.is_dir() and (d / "manifest.json").exists()
    ], key=lambda d: d.name)

    if not dirs:
        print("No snapshots found.")
        return

    session_snaps = [d for d in dirs if d.name.startswith("Session_")]
    rollback_snaps = [d for d in dirs if d.name.startswith("pre_rollback")]

    if session_snaps:
        print("SESSION SNAPSHOTS:")
        print("-" * 60)
        for d in session_snaps:
            with open(d / "manifest.json", "r", encoding="utf-8") as f:
                m = json.load(f)
            session = m.get("session_number", "?")
            date = m.get("timestamp", "?")[:10]
            floor = m.get("floor", "?")
            files = m.get("file_count", "?")
            notes = m.get("notes", "")
            level_ups = m.get("level_ups", [])
            dossier_archives = m.get("dossier_archives", [])

            print(f"  Session {session:>3}  |  {date}  |  Floor {floor}  |  {files} files")
            if level_ups:
                lu_str = ", ".join(f"{lu['character']}→Lv{lu['new_level']}" for lu in level_ups)
                print(f"             |  Level-ups: {lu_str}")
            if dossier_archives:
                print(f"             |  Dossier archives: {', '.join(dossier_archives)}")
            if notes:
                print(f"             |  Notes: {notes}")

            if detail:
                for fname in m.get("files", []):
                    print(f"             |    {fname}")

        print()

    if rollback_snaps:
        print("PRE-ROLLBACK ARCHIVES:")
        print("-" * 60)
        for d in rollback_snaps:
            with open(d / "manifest.json", "r", encoding="utf-8") as f:
                m = json.load(f)
            target = m.get("rollback_target", "?")
            date = m.get("timestamp", "?")[:10]
            files = m.get("file_count", "?")
            reason = m.get("reason", "")
            print(f"  {d.name}")
            print(f"    Rolled back to Session {target}  |  {date}  |  {files} files")
            if reason:
                print(f"    Reason: {reason}")
        print()


def show_rollback_history():
    """Show the rollback event log."""
    if not ROLLBACK_LOG.exists():
        print("No rollback history. No rollbacks have been performed.")
        return

    with open(ROLLBACK_LOG, "r", encoding="utf-8") as f:
        history = json.load(f)

    if not history:
        print("Rollback history is empty.")
        return

    print("ROLLBACK HISTORY:")
    print("-" * 60)
    for i, entry in enumerate(history, 1):
        date = entry.get("timestamp", "?")[:19]
        target = entry.get("target_session", "?")
        reason = entry.get("reason", "none given")
        archive = entry.get("pre_rollback_archive", "?")
        files = entry.get("files_restored", "?")
        warnings = entry.get("warnings", [])

        print(f"  #{i}  {date}")
        print(f"    Rolled back to: Session {target}")
        print(f"    Files restored: {files}")
        print(f"    Archive: {archive}")
        if reason:
            print(f"    Reason: {reason}")
        if warnings:
            for w in warnings:
                print(f"    Warning: {w}")
        print()


def main():
    parser = argparse.ArgumentParser(description="DCC v2 Snapshot Status")
    parser.add_argument("--detail", action="store_true", help="Show file lists in snapshots")
    parser.add_argument("--history", action="store_true", help="Show rollback history")
    args = parser.parse_args()

    if args.history:
        show_rollback_history()
    else:
        list_snapshots(detail=args.detail)


if __name__ == "__main__":
    main()
