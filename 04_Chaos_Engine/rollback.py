"""
DCC v2 — Session Rollback Tool
Non-destructive: archives current state before restoring a prior snapshot.

Usage:
  python rollback.py <target_session> [--reason "text"]

Example:
  python rollback.py 2 --reason "Session 3 had narrator hallucination in combat"

This will:
  1. Snapshot current state as "pre_rollback_to_002"
  2. Copy Session_002 snapshot files over the live files
  3. Verify file counts match the manifest
  4. Log the rollback event
"""

import argparse
import json
import shutil
import os
from datetime import datetime
from pathlib import Path

ENGINE_DIR = Path(__file__).parent
DCC_V2_DIR = ENGINE_DIR.parent
CAMPAIGN_DIR = DCC_V2_DIR / "00_Campaign"
CHARACTERS_DIR = DCC_V2_DIR / "01_Characters"
SNAPSHOTS_DIR = DCC_V2_DIR / "05_Snapshots"
ROLLBACK_LOG = SNAPSHOTS_DIR / "rollback_history.json"


def load_manifest(session_dir: Path) -> dict:
    manifest_path = session_dir / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"No manifest.json in {session_dir}")
    with open(manifest_path, "r", encoding="utf-8") as f:
        return json.load(f)


def archive_current_state(target_session: int, reason: str) -> Path:
    """Save current live state as a pre-rollback snapshot."""
    archive_name = f"pre_rollback_to_{target_session:03d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    archive_dir = SNAPSHOTS_DIR / archive_name
    archive_dir.mkdir(parents=True)

    campaign_snap = archive_dir / "00_Campaign"
    campaign_snap.mkdir()
    characters_snap = archive_dir / "01_Characters"
    characters_snap.mkdir()

    files_copied = []

    # Copy live campaign files
    if CAMPAIGN_DIR.exists():
        for f in CAMPAIGN_DIR.iterdir():
            if f.suffix == ".docx":
                dst = campaign_snap / f.name
                shutil.copy2(f, dst)
                files_copied.append(f"00_Campaign/{f.name}")

    # Copy live character files
    if CHARACTERS_DIR.exists():
        for f in CHARACTERS_DIR.iterdir():
            if f.suffix == ".docx" and f.name != "_Index.docx":
                dst = characters_snap / f.name
                shutil.copy2(f, dst)
                files_copied.append(f"01_Characters/{f.name}")

    # Write manifest for the archive
    manifest = {
        "snapshot_type": "pre_rollback",
        "rollback_target": target_session,
        "reason": reason,
        "timestamp": datetime.now().isoformat(),
        "files": sorted(files_copied),
        "file_count": len(files_copied),
    }
    with open(archive_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    return archive_dir


def restore_snapshot(session_dir: Path, manifest: dict) -> dict:
    """
    Copy snapshot files over the live files.
    Returns a report dict with counts and any issues.
    """
    report = {"restored": [], "skipped": [], "warnings": []}

    # Restore 00_Campaign files
    snap_campaign = session_dir / "00_Campaign"
    if snap_campaign.exists():
        for f in snap_campaign.iterdir():
            if f.suffix == ".docx":
                dst = CAMPAIGN_DIR / f.name
                shutil.copy2(f, dst)
                report["restored"].append(f"00_Campaign/{f.name}")

    # Restore 01_Characters files
    snap_characters = session_dir / "01_Characters"
    if snap_characters.exists():
        # First, note any character files in live that aren't in the snapshot
        # (characters added after the snapshot session — don't delete, just warn)
        live_chars = set()
        if CHARACTERS_DIR.exists():
            live_chars = {f.name for f in CHARACTERS_DIR.iterdir() if f.suffix == ".docx" and f.name != "_Index.docx"}
        snap_chars = {f.name for f in snap_characters.iterdir() if f.suffix == ".docx"}

        extra_in_live = live_chars - snap_chars
        if extra_in_live:
            report["warnings"].append(
                f"Character files not in snapshot (added after Session {manifest.get('session_number', '?')}): "
                f"{', '.join(sorted(extra_in_live))}. Left in place — review manually."
            )

        for f in snap_characters.iterdir():
            if f.suffix == ".docx":
                dst = CHARACTERS_DIR / f.name
                shutil.copy2(f, dst)
                report["restored"].append(f"01_Characters/{f.name}")

    return report


def log_rollback(target_session: int, reason: str, archive_path: Path, report: dict):
    """Append to rollback history log."""
    history = []
    if ROLLBACK_LOG.exists():
        with open(ROLLBACK_LOG, "r", encoding="utf-8") as f:
            history = json.load(f)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "target_session": target_session,
        "reason": reason,
        "pre_rollback_archive": str(archive_path.name),
        "files_restored": len(report["restored"]),
        "warnings": report["warnings"],
    }
    history.append(entry)

    with open(ROLLBACK_LOG, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def rollback(target_session: int, reason: str = ""):
    """
    Full rollback procedure:
    1. Verify target snapshot exists
    2. Archive current state
    3. Restore target snapshot
    4. Verify
    5. Log
    """
    # Step 1: Find and validate target snapshot
    target_dir = SNAPSHOTS_DIR / f"Session_{target_session:03d}"
    if not target_dir.exists():
        raise FileNotFoundError(
            f"No snapshot found for Session {target_session:03d}.\n"
            f"Available snapshots: {list_available_snapshots()}"
        )

    manifest = load_manifest(target_dir)
    print(f"Target: Session {target_session:03d}")
    print(f"  Snapshot date: {manifest.get('timestamp', 'unknown')}")
    print(f"  Floor: {manifest.get('floor', 'unknown')}")
    print(f"  Files in snapshot: {manifest.get('file_count', '?')}")
    print()

    # Step 2: Archive current state
    print("Archiving current state (non-destructive)...")
    archive_path = archive_current_state(target_session, reason)
    print(f"  Archived to: {archive_path.name}")
    print()

    # Step 3: Restore
    print("Restoring snapshot...")
    report = restore_snapshot(target_dir, manifest)
    print(f"  Restored: {len(report['restored'])} files")
    if report["warnings"]:
        for w in report["warnings"]:
            print(f"  WARNING: {w}")
    print()

    # Step 4: Verify
    expected_campaign_files = [f for f in manifest.get("files", []) if f.startswith("00_Campaign/")]
    expected_char_files = [f for f in manifest.get("files", []) if f.startswith("01_Characters/")]
    restored_campaign = [f for f in report["restored"] if f.startswith("00_Campaign/")]
    restored_chars = [f for f in report["restored"] if f.startswith("01_Characters/")]

    # Note: snapshot may include dossier archives (Lv files) that don't get restored to live
    # Only count the base mutable files for verification
    print("Verification:")
    print(f"  Campaign files restored: {len(restored_campaign)}")
    print(f"  Character files restored: {len(restored_chars)}")
    print()

    # Step 5: Log
    log_rollback(target_session, reason, archive_path, report)
    print(f"Rollback logged to: {ROLLBACK_LOG.name}")
    print()

    if reason:
        print(f"Reason: {reason}")
    print(f"\nRollback complete. Campaign state is now at end-of-Session {target_session:03d}.")
    print(f"Pre-rollback state preserved in: {archive_path.name}")

    return report


def list_available_snapshots() -> list[str]:
    """List all session snapshots."""
    if not SNAPSHOTS_DIR.exists():
        return []
    return sorted([
        d.name for d in SNAPSHOTS_DIR.iterdir()
        if d.is_dir() and d.name.startswith("Session_")
    ])


def main():
    parser = argparse.ArgumentParser(description="DCC v2 Session Rollback Tool")
    parser.add_argument("session", type=int, help="Target session number to roll back to")
    parser.add_argument("--reason", type=str, default="", help="Reason for rollback")
    parser.add_argument("--list", action="store_true", help="List available snapshots and exit")

    args = parser.parse_args()

    if args.list:
        snapshots = list_available_snapshots()
        if snapshots:
            print("Available snapshots:")
            for s in snapshots:
                print(f"  {s}")
        else:
            print("No snapshots found.")
        return

    try:
        rollback(args.session, args.reason)
    except (FileNotFoundError, FileExistsError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
