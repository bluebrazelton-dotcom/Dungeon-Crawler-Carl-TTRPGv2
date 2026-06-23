MASTER FILE INDEX
Load this first. Every document in the campaign, what it does, and when to load it.
This index is the narrator's table of contents for the entire campaign state. Load it at the start of every session to know what exists and where to find it. Then load the specific documents needed for the session type.

# DCC_v2/ (Root)
DCC_v2_Architecture_Blueprint.docx -- Complete system design. Reference only, not loaded during play.
Master_File_Index.docx -- THIS DOCUMENT. Load every session.

# 00_Campaign/ -- Core Campaign Documents
Persistent documents maintained across the entire campaign.

Mechanical Reference
  Combat_Cheat_Sheet.docx -- Versioned source of truth for all mechanics. LOAD EVERY PLAY SESSION.
  Chat_System.docx -- Chat affordance spec (Crawlers, NPCs, sponsors, AI). Load every Play session if any contacts have been added; otherwise on demand.

Narrative Continuity
Campaign_Spine.docx -- One paragraph per floor, narrative arc. Play sessions: load current floor ±2 only (~500 words). Story sessions: load full Spine.
  Thread_Tracker.docx -- Open threads with pressure ratings. Load every Story + Play session.
Moments_Log.docx -- Curated emotional moments (max 30). Play sessions: load top 15 entries (~750 words). Full log available on demand.
  Voice_Bible.docx -- Character voice samples and tone. Load every Play session.

Character Tracking
  Crawler_Dossiers.docx -- Doug and Casey sheets with XP tracking. Load every Play session.
  Character_Index.docx -- One-line NPC roster. Load every session to know who exists.

Logistics and World State
  Master_Inventory.docx -- Every item ever acquired with status tracking. Load every Play session.
  Pet_Companion_Registry.docx -- Non-NPC entities with the party. Load if any companions active.
  Crafting_Log.docx -- Item transformation history. Load when crafting is relevant (Floor 3+).
  Reputation_Ledger.docx -- Sponsor/faction/institutional relationships. Load when social/sponsor scenes expected.
  Contract_Obligation_Log.docx -- Promises, debts, deadlines. Load every Play session (check for overdue).
  Dungeon_State_Log.docx -- Persistent environmental changes by floor. Load current floor's entries.
  Discovery_Index.docx -- Learned knowledge, codes, lore. Load when exploration/puzzles expected.

Session Management
Build_Session_Protocol.docx, Story_Session_Protocol.docx, Play_Session_Protocol.docx -- Step-by-step protocols, one per session type. Load only the one you need.
  Health_Check_Template.docx -- Copy-and-fill for end-of-session diagnostics.

# 01_Characters/ -- Per-Character Files
Individual files for named NPCs. Load only the 4-6 active characters per session. Check Character_Index.docx to determine who is relevant.
[No character files yet -- populated during Floor 1 Build Session]

# 02_Floors/ -- Per-Floor Packages
Self-contained design packages built during Build Sessions. Each floor's subfolder contains: Floor Design Doc, Chaos Engine Tables, Loot Tables, NPC Introductions.
[No floor packages yet -- Floor_01/ built during first Build Session]

# 03_Sessions/ -- Session-Specific Documents
Save files, handoffs (capped at 200-300 words, structured template), recaps, and health checks. Load only the most recent save + handoff at session start.
[No session documents yet -- populated after Play Session 001]

# 04_Chaos_Engine/ -- RNG Tooling
Python scripts for dice rolling, loot generation, chaos clock, encounter modification, context checkpoints, session snapshots, and rollback. Fully built.
Python scripts and JSON data files for external RNG: event table roller, chaos clock, loot roller, encounter modifiers, context checkpoint system, session snapshot and rollback tools. See TABLE_FORMAT.md for floor table population guide.

05_Snapshots/ -- Session State Archives
Versioned snapshots of all mutable campaign state, taken at the end of every play session. Each snapshot contains a full copy of 00_Campaign/ and 01_Characters/ files plus a manifest.json with session metadata. Used for rollback if a session produces errors or hallucinations. Also contains pre-rollback archives (non-destructive -- rolling back never deletes data).
# Loading Guide by Session Type

## Build Session -- Load:
- Master File Index, Combat Cheat Sheet, Character Index, relevant prior floor packages for reference
## Story Session -- Load:
- Master File Index
- Campaign Spine
- Thread Tracker
- Moments Log
- Voice Bible
- Character Index
- Contract/Obligation Log (check for overdue)
## Play Session -- Load:
- Master File Index (scan, then set aside)
- Combat Cheat Sheet
- Current save file + Session Handoff
- Active character files (4-6 from 01_Characters/)
- Current Floor Design Doc (Chaos Engine tables are JSON consumed by scripts, not loaded as context)
- Thread Tracker
- Moments Log
- Voice Bible
- Campaign Spine (current + adjacent floors)
- Crawler Dossiers
- Master Inventory
- Contract/Obligation Log
- Pet/Companion Registry (if any active companions)

Load on demand during play: Discovery Index, Dungeon State Log, Crafting Log, Reputation Ledger, additional character files

# Floor 1 Package — Added May 18, 2026
02_Floors/Floor_01/Floor_01_Design_Doc.docx — Floor 1 design (narrator-only sections marked).
02_Floors/Floor_01/Floor_01_Loot_Tables.docx — Loot narrative companion.
02_Floors/Floor_01/floor_01_tables.json — Chaos engine tables (event tables, chaos clock, loot, encounter modifiers).
01_Characters/Garland_Cress.docx — Mall manager NPC file.
01_Characters/Tasha_Okonkwo.docx — "Kid Who Can't Die" NPC file.
01_Characters/Harvey_Pennybrook.docx — Almond vendor NPC file.
01_Characters/Food_Court_People.docx — Food Court trio NPC file.
Combat_Cheat_Sheet.docx updated to v1.1 (added Loyalty Card System, Section 14).
Campaign_Spine.docx, Voice_Bible.docx, Thread_Tracker.docx — Floor 1 seed entries added.
05_Snapshots/ folder created (per blueprint requirement; previously missing).
## Floor 1 Story Session — Updates (May 18, 2026)
Campaign_Spine.docx — Floor 1 paragraph refined to walk the three questions (story, advancement, emotional target).
Thread_Tracker.docx — Floor 1 thread pressures recalibrated against pre-Play-Session-1 baseline. T-001 split into narrator-pressure vs player-pressure. T-004 (Pennybrook NPC-presence) advanced to 2/5 — locked as first NPC met in Play Session 1.
Voice_Bible.docx — Story Session voice notes appended: emotional register and 'never do this' for all Floor 1 voices (Walda surface + real, Garland, Tasha, Pennybrook, Food Court trio). NABRZ discipline note for @SAFE_MOMS_OF_NABRZ tied to Chaos Clock #25.
Character_Index.docx — Play Session 1 active cast marked (all 4 NPC files, 6 individuals). Crawler entry updated to DEFERRED with Session-1-opens-with-character-creation flag.
03_Sessions/Session_001_Handoff.docx — drafted (first Play Session briefing, 200-300 words).
## Floor 1 Story Session — Addendum (Crawler Dossiers Built, May 18, 2026)
Crawler_Dossiers.docx — Doug and Casey built per Story Session character-creation pass. Doug: Substitute Teacher (custom Job), CHA 6 / CON 7, HP 23, MP 8, 10 starting skills. Casey: Trivia Night Host (custom Job), CHA 6 / INT 7, HP 17, MP 14, 10 starting skills. Both custom Jobs use the GDD §8.3 framework (+1 to two attributes, two skills at Level 4).
Character_Index.docx — Crawler entry promoted from DEFERRED to ACTIVE.
Session_001_Handoff.docx — revised; no longer opens with character creation. Session 001 starts in-fiction at Zone A spawn.
## Floor 1 Story Session — Addendum (Chat System Added, May 18, 2026)
Chat_System.docx (NEW, 00_Campaign/) — Campaign-wide chat affordance specification. Defines contact list rules (meet-once, chat-forever), range (intra-floor unlimited, inter-floor blocked except via Personal Space), rendering format ('Character (in chat):'), audience visibility (private by default; Open Channel and Premium DM monetization), AI intrusion rules (anytime, bypasses contact list), and narrator pacing (1-3 pings per session, interrupt-driven). Floor 1 NPC chat flags included for the four named NPCs.
Combat_Cheat_Sheet.docx — Bumped to v1.2. Added Section 15 (Chat System summary, pointing at the full spec). No Section 14 (Loyalty Card) changes.
Play_Session_Protocol.docx — Load list updated to include Chat_System.docx when contacts are active; load-on-demand otherwise.
## Play Session 002 — Updates (May 23, 2026)
03_Sessions/Session_002_Save.docx — Session 002 save file. Party on upper concourse, Sears cleared, first combat complete.
03_Sessions/Session_002_Health_Check.docx — Session 002 narrator health check. Mechanical Consistency YELLOW (improvised rulings). Chaos Engine YELLOW (two sessions, zero fires). All others GREEN.
03_Sessions/Session_003_Handoff.docx — Session 002→003 handoff. Chaos clock MUST fire. Spencer’s display case key acquired. Two paths to Sub-Level available.
Crawler_Dossiers.docx — Updated. Skill advancements: Doug (Improvisation 6, Bathroom 2, Asking Forgiveness 3, Crowd Coordination 2), Casey (Genre Recognition 6, Spotting Inconsistencies 2). Doug Charter Member (46★). First Followers earned (Doug 29, Casey 24).
Master_Inventory.docx — Updated. New items: Mannequin Arm x2, Fire Hose, Sears Display Case Key, Sears 20-Year Service Pin. Dinosaur Keychain returned to Tasha.
Thread_Tracker.docx — Updated. T-005 (The Sears) at 5/5 (cleared). T-008 (Loyalty Tally) at 4/5 (Charter Member). T-006 at 3/5 (freight elevator alternate route).
Moments_Log.docx — 5 new entries added (10 total). Escalator conversion, dinosaur keychain, mannequin arm combat, fire hose Crescendo, Dana’s quiet beat.
Character_Index.docx — Updated. Tasha formally met and extracted from Sears. Added to party contacts.
## Play Session 003 — Updates (May 23, 2026)
03_Sessions/Session_003_Save.docx — Session 003 save file. Party in food court. Ruth/Walda identity revealed, stepped down. Penny brought online. Garland knows his state. Boss encounter bypassed.
03_Sessions/Session_003_Health_Check.docx — Session 003 narrator health check. Chaos Engine RED (three sessions, zero fires). Mechanical Consistency YELLOW. Narrative Coherence YELLOW. All others GREEN.
03_Sessions/Session_004_Handoff.docx — Session 003→004 handoff. Story Session recommended. Dungeon contract unresolved. Chaos clock must fire.
Crawler_Dossiers.docx — Updated. Skill advancements: Doug (Reading the Room 6), Casey (Genre Recognition 7, Spotting Inconsistencies 3). Doug 290 Viewers, 52 Loyalty (Charter). Casey 250 Viewers, 32 Loyalty (Charter).
Master_Inventory.docx — Updated. 16 new items: Tab, Spencer’s display case contents (nametag pin, lava lamp, snowglobe), Ruth’s artifacts (nametag, photo, note, badge), Garland’s artifacts (note, lanyard, radio), first-aid kit, flip-flop keychain, Sal’s Sub-Level key, Sears lockbox photos.
Thread_Tracker.docx — Updated. T-002 at 4/5 (Walda identity revealed). T-003 at 5/5 (Garland knows). T-006 at 5/5 (both keys acquired). T-008 updated (both Crawlers Charter tier).
Moments_Log.docx — 5 new entries added (15 total). Badge bypass, pineapple philosophy, Ruth’s real voice, Penny’s naming.
Character_Index.docx — Updated. Penny and Ruth added as new character entries. Garland status updated (truth unlocked). Active cast for Session 004 expanded.
Play Session 004 — Updates (May 23, 2026)
03_Sessions/Session_004_Save.docx — Session 004 save file. Floor 1 COMPLETE. Boss encounter resolved via Compliance Action against Badge #1 (emergent). Party in Floor 2 stairwell.
03_Sessions/Session_004_Health_Check.docx — Session 004 narrator health check. Chaos Engine GREEN (debt resolved). Mechanical Consistency YELLOW. Document Health YELLOW. Narrative Coherence YELLOW. All others GREEN.
03_Sessions/Session_005_Handoff.docx — Session 004 to 005 handoff. BUILD SESSION REQUIRED for Floor 2. Story Session items pending.
Crawler_Dossiers.docx — Updated. Skill advancements: Doug (Improvisation 7, De-escalation 3), Casey (Genre Recognition 8, Audience Management 5). Doug 2480 Viewers, 401 Followers. Casey 2480 Viewers, 396 Followers.
Master_Inventory.docx — Updated. 6 new items: Badge #1 Maglite, Sal Lighter, Dana Socks, Tasha Mall Keychain, Sal Farewell Pizza, Unit 7 Frosting Recipe. 2 items consumed.
Thread_Tracker.docx — Updated. T-002, T-003, T-005, T-006, T-008 resolved. T-009 (Badge #1), T-010 (Compliance Action), T-011 (sponsor contract) added. T-001 still unresolved.
Moments_Log.docx — 5 new entries added (20 total). Joy buzzer boss opener, mannequin Three Stooges, almond absorption, Dana There you are.
Character_Index.docx — Updated. Badge #1 added as emergent NPC. All Floor 1 NPCs marked FLOOR 1 RESIDENT. Floor 2 cast TBD.
# Floor 2 Package — Added May 23, 2026
02_Floors/Floor_02/Floor_02_Design_Doc.docx — Floor 2 design (narrator-only sections marked). Theme: Customer Service. Boss: The Escalation (Charles).
02_Floors/Floor_02/Floor_02_Loot_Tables.docx — Loot narrative companion. Tag synergies: call_center, headset, corporate, caffeine, performance_token.
02_Floors/Floor_02/floor_02_tables.json — Chaos engine tables (event tables, chaos clock with 13 events, loot, encounter modifiers, escalation_lair sub-table).
Floor_2_Build_Handoff.docx (DCC_v2/ root) — Handoff into Floor 2 Story Session. Deliverables listed.
Floor_2_Story_Handoff.docx (DCC_v2/ root) — Handoff into Floor 2 Play Sessions. 4-6 session narrative arc, NPC introduction order, emotional beats.
02_Floors/_Index.docx — Updated. Floor 1 marked COMPLETE; Floor 2 entry added as SEALED, ready for Story Session.
Carries forward: T-001 (Tasha's mother), T-010 (Compliance Action precedent), T-011 (First Sponsor Contract). Permanent death enabled on Floor 2.
Requires next: Combat_Cheat_Sheet.docx v1.3 update (CSAT/Call Queue, Performance Tokens, permanent death clarification). Voice_Bible.docx Floor 2 supplement (PHRYNE seeds + 5 NPC voices + Charles Phase 1/2). 01_Characters/Floor_02/ NPC files (5).
