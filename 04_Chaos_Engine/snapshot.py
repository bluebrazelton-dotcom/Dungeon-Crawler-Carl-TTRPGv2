"""
DCC v2 — Session Snapshot Tool
Runs at session end. Copies all mutable campaign state into a versioned snapshot folder.

Usage:
  python snapshot.py <session_number> [--floor N] [--level-up CHAR:LEVEL] [--notes "text"]

Examples:
  python snapshot.py 1 --floor 1
  python snapshot.py 3 --floor 1 --level-up Doug:7 --level-up Casey:6 --notes "Boss fight complete"
"""

import argparse
import json
import shutil
import os
from datetime import datetime
from pathlib import Path

# Paths relative to this script's location (04_Chaos_Engine/)
ENGINE_DIR = Path(__file__).parent
DCC_V2_DIR = ENGINE_DIR.parent
CAMPAIGN_DIR = DCC_V2_DIR / "00_Campaign"
CHARACTERS_DIR = DCC_V2_DIR / "01_Characters"
SNAPSHOTS_DIR = DCC_V2_DIR / "05_Snapshots"

# All mutable files in 00_Campaign/ that get snapshotted
CAMPAIGN_MUTABLE = [
    "Campaign_Spine.docx",
    "Character_Index.docx",
    "Chat_System.docx",
    "Combat_Cheat_Sheet.docx",
    "Contract_Obligation_Log.docx",
    "Crafting_Log.docx",
    "Crawler_Dossiers.docx",
    "Discovery_Index.docx",
    "Dungeon_State_Log.docx",
    "Master_Inventory.docx",
    "Moments_Log.docx",
    "Pet_Companion_Registry.docx",
    "Reputation_Ledger.docx",
    "Thread_Tracker.docx",
    "Voice_Bible.docx",
]

# Files in 00_Campaign/ that are static (not snapshotted)
CAMPAIGN_STATIC = [
    "Health_Check_Template.docx",
    "Session_Startup_Protocol.docx",
]


def get_session_dir(session_number: int) -> Path:
    return SNAPSHOTS_DIR / f"Session_{session_number:03d}"


def snapshot_session(
    session_number: int,
    floor: int | None = None,
    level_ups: list[tuple[str, int]] | None = None,
    notes: str = "",
) -> Path:
    """
    Create a full snapshot of all mutable campaign state.
    Returns the path to the snapshot directory.
    """
    session_dir = get_session_dir(session_number)

    if session_dir.exists():
        raise FileExistsError(
            f"Snapshot for Session {session_number:03d} already exists at {session_dir}.\n"
            f"If you need to re-snapshot, delete or rename the existing one first."
        )

    # Create snapshot directory structure
    session_dir.mkdir(parents=True)
    campaign_snap = session_dir / "00_Campaign"
    campaign_snap.mkdir()
    characters_snap = session_dir / "01_Characters"
    characters_snap.mkdir()

    files_copied = []

    # Copy all mutable campaign files
    for filename in CAMPAIGN_MUTABLE:
        src = CAMPAIGN_DIR / filename
        if src.exists():
            dst = campaign_snap / filename
            shutil.copy2(src, dst)
            files_copied.append(f"00_Campaign/{filename}")

    # Handle dossier level-up archiving
    dossier_archives = []
    if level_ups:
        dossier_src = CAMPAIGN_DIR / "Crawler_Dossiers.docx"
        if dossier_src.exists():
            for char_name, new_level in level_ups:
                old_level = new_level - 1
                archive_name = f"Crawler_Dossiers_Lv{old_level:02d}_{char_name}.docx"
                archive_dst = campaign_snap / archive_name
                shutil.copy2(dossier_src, archive_dst)
                dossier_archives.append(archive_name)
                files_copied.append(f"00_Campaign/{archive_name}")

    # Copy all character files (everything in 01_Characters/ except _Index.docx)
    if CHARACTERS_DIR.exists():
        for f in CHARACTERS_DIR.iterdir():
            if f.suffix == ".docx" and f.name != "_Index.docx":
                dst = characters_snap / f.name
                shutil.copy2(f, dst)
                files_copied.append(f"01_Characters/{f.name}")

    # Copy health check if one was generated for this session
    sessions_dir = DCC_V2_DIR / "03_Sessions"
    if sessions_dir.exists():
        health_check = sessions_dir / f"Health_Check_{session_number:03d}.docx"
        if health_check.exists():
            shutil.copy2(health_check, session_dir / health_check.name)
            files_copied.append(health_check.name)

        # Also grab the save file and handoff if they exist
        for prefix in ["Save_Session_", "Session_Handoff_"]:
            candidate = sessions_dir / f"{prefix}{session_number:03d}.docx"
            if candidate.exists():
                shutil.copy2(candidate, session_dir / candidate.name)
                files_copied.append(candidate.name)

    # Generate manifest
    manifest = {
        "session_number": session_number,
        "timestamp": datetime.now().isoformat(),
        "floor": floor,
        "level_ups": [{"character": c, "new_level": l} for c, l in (level_ups or [])],
        "dossier_archives": dossier_archives,
        "notes": notes,
        "files": sorted(files_copied),
        "file_count": len(files_copied),
        "snapshot_type": "session_end",
    }

    manifest_path = session_dir / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    return session_dir


def main():
    parser = argparse.ArgumentParser(description="DCC v2 Session Snapshot Tool")
    parser.add_argument("session", type=int, help="Session number (e.g., 1, 2, 3)")
    parser.add_argument("--floor", type=int, default=None, help="Current floor number")
    parser.add_argument(
        "--level-up",
        action="append",
        metavar="CHAR:LEVEL",
        help="Character level-up (e.g., Doug:7). Repeatable.",
    )
    parser.add_argument("--notes", type=str, default="", help="Session notes for the manifest")

    args = parser.parse_args()

    # Parse level-ups
    level_ups = None
    if args.level_up:
        level_ups = []
        for lu in args.level_up:
            parts = lu.split(":")
            if len(parts) != 2:
                print(f"Error: level-up must be CHAR:LEVEL, got '{lu}'")
                return
            level_ups.append((parts[0], int(parts[1])))

    try:
        snap_dir = snapshot_session(args.session, args.floor, level_ups, args.notes)
        # Read back manifest to confirm
        with open(snap_dir / "manifest.json", "r") as f:
            manifest = json.load(f)

        print(f"Snapshot created: Session {args.session:03d}")
        print(f"  Location: {snap_dir}")
        print(f"  Files: {manifest['file_count']}")
        if manifest["floor"]:
            print(f"  Floor: {manifest['floor']}")
        if manifest["level_ups"]:
            for lu in manifest["level_ups"]:
                print(f"  Level-up: {lu['character']} → Level {lu['new_level']}")
        if manifest["dossier_archives"]:
            for da in manifest["dossier_archives"]:
                print(f"  Dossier archived: {da}")
        if manifest["notes"]:
            print(f"  Notes: {manifest['notes']}")
        print("  Done.")

    except (FileExistsError, FileNotFoundError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
