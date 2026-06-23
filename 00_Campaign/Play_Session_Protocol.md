PLAY SESSION PROTOCOL
Run the actual game. Load pre-built world, integrate chaos, maintain voices.

# Load Phase
Target: 10,000-12,000 words. Flag if over 12,000.

Always load:
- Master File Index (scan, then set aside)
- Combat Cheat Sheet
- Current save file + Session Handoff
- Crawler Dossiers
- Active character files (4-6 from 01_Characters/)
- Current Floor Design Doc + Chaos Engine Tables
- Thread Tracker
- Moments Log (load top 15 entries by relevance, ~750 words max; full log on demand)
- Voice Bible
- Chat System (campaign-wide chat rules; rendering format, AI intrusion, NPC flags)
- Campaign Spine (current floor ±2 only, ~500 words max; full Spine available on demand)
- Master Inventory (scan for equipped items at start; full load on demand for loot/shopping)
- Contract/Obligation Log (scan for overdue at start; full load on demand when obligations arise)

Load if relevant:
- Pet/Companion Registry -- if any companions are ACTIVE
- Reputation Ledger -- if sponsor/faction scenes expected
- Discovery Index -- if exploration or puzzle-solving expected
- Dungeon State Log -- current floor entries, if returning to modified areas

Load on demand during play:
Additional character files, Crafting Log, prior floor state entries, session transcripts (max 2-3 retrievals)
# Pre-Play Setup
1. If pre-rolled RNG sequence: Doug rolls 10-15 numbers.
2. Narrator delivers brief recap (2-3 sentences) and confirms party position.
3. Verify: Are all ACTIVE pets/companions accounted for? Any overdue obligations?
4. Play begins.
# During Play
- Chaos engine triggers fire per floor tables. Narrator honors ALL results.
- Doug rolls dice at narrator prompts for loot, events, encounters.
- Narrator may retrieve prior session transcripts (max 2-3 per session).
- If unplanned character enters scene, load their file on demand.
- New items: add to Master Inventory immediately (don't wait for session end).
- New discoveries: note for Discovery Index update at session end.
- New obligations: note for Contract/Obligation Log update at session end.

Context Checkpoint — every 45-60 minutes or 15-20 exchanges, whichever comes first. Five-question self-check (voice, mechanics, threads, position, continuity). Output one of three signals:
- STABLE — all checks pass. Continue play. Next checkpoint in 45-60 min.
- STRAINED — wrap current scene within 15-20 minutes, then save. Note which checks failed — they feed into the end-of-session Health Check.
- SAVE NOW — stop play at next natural pause. Execute end-of-session sequence immediately.
The narrator cannot skip, delay, or downplay a checkpoint result. Same hard rule as chaos engine integration.
# End-of-Session Sequence
Order matters. Health Check runs first (while full session is in context). Snapshot runs last (captures everything). Nothing between these steps is optional except the Recap.

1. Run Narrator Health Check. Eight diagnostic areas (including Narrative Coherence), traffic light ratings. If any mid-session checkpoint flagged STRAINED, reference it under Context Load. Save report to 03_Sessions/.
2. Generate updated save file. Reference Cheat Sheet version. Save to 03_Sessions/.
3. Run skill advancement rolls for all skills used meaningfully this session.
4. Update all tracker documents: Crawler Dossiers (stats, equipment, HP/MP, XP), Master Inventory, Pet/Companion Registry, Contract/Obligation Log, Dungeon State Log, Discovery Index. Skip any that had no changes this session.
5. Flag thread changes, character developments, mechanical issues for next Story Session.
6. Generate Session Handoff (use template in 03_Sessions/, cap at 200-300 words) (or note if Story/Maintenance session needed first).
7. Update Master File Index and 03_Sessions/_Index.docx with new session entries.
8. Optional: generate Recap for player enjoyment.
9. Run session snapshot: python snapshot.py <session_number> --floor <N> [--level-up CHAR:LEVEL]. This archives all mutable campaign state for rollback capability. The snapshot captures the final state of everything updated in steps 1-8.
For Health Check: use Health_Check_Template.docx (8 diagnostic areas, traffic light system). Run it as step 1 of this sequence while the full session is still in context.
