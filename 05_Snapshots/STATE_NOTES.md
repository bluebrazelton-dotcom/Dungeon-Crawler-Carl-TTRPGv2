# 05_Snapshots — State Notes

## Snapshot history at Session 0

Two pre-Session-1 snapshots exist:

1. **`Session_000/`** — original. Created 2026-05-18 14:34. Captures state AFTER Floor 1 Build + Floor 1 Story Session + Crawler dossier build, but BEFORE the Chat System addendum (Chat_System.docx, Combat_Cheat_Sheet v1.2). 18 files.

2. **`Session_000_post_chat_system_*/`** — addendum. Created 2026-05-18 14:45. Captures the *current* pre-Session-1 baseline, including the Chat System addition. 20 files (adds Chat_System.docx and Session_001_Handoff.docx).

The filesystem mount does not permit deleting the original Session_000 snapshot, so both coexist. **If rolling back to pre-Session-1 state, restore from the addendum directory, not Session_000.**

The snapshot.py `CAMPAIGN_MUTABLE` list has been updated to include Chat_System.docx, so all future snapshots (Session_001 onward) will capture it correctly.

This note can be removed once Session_001 ends and a real Session_001 snapshot exists with the Chat System in it.
