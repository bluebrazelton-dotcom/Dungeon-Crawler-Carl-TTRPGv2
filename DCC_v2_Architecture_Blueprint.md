DUNGEON CRAWLER CARL
THE GAME
v2.0 Architecture Blueprint
April 2026
This document defines the architecture for rebuilding the DCC campaign with improved memory stability, structured creativity, external randomness, and narrative continuity across an 18-floor dungeon. It is a blueprint for Doug to review before any files are built.

# 1. Design Philosophy
The v1 campaign proved that an AI narrator can run a mechanically complex, emotionally resonant TTRPG across multiple sessions. It also proved that the architecture breaks at scale. The post mortem identified five categories of failure: voice drift, mechanical drift, thread amnesia, contextual compression, and emotional state loss. All five trace to a single root cause: each session starts a new conversation with no persistent memory.
The v2 architecture does not solve this constraint. What it does is restructure every piece of the campaign to work within the constraint rather than against it. Three principles guide every design decision:
- Separate what changes from what persists. Mechanics are stable; they belong in versioned reference documents loaded every session. Narrative is cumulative; it belongs in structured logs that grow across sessions. Creativity is volatile; it belongs in pre-built floor packages that contain surprises neither the narrator nor the player fully controls.
- Take randomness out of the narrator's hands. The narrator's generation is biased toward narrative coherence. Dungeon Crawler Carl's identity is chaos that characters make meaning from. External RNG systems force the narrator to integrate results it would never have generated, producing genuine unpredictability.
- Build the world before you play in it. The v1 campaign improvised everything beyond Floor 1 during live play. The v2 architecture separates world-building, storytelling, and gameplay into distinct session types so the narrator arrives at each play session with a pre-existing world to navigate, not an empty room to invent.
# 2. The Three-Session Framework
Every floor of the dungeon is produced through three types of session, run in order. Each type has a distinct purpose, a different relationship between Doug and the narrator, and different document outputs.
## 2.1 Build Sessions (World-Building)
Purpose: Design the floor's physical space, mechanical systems, encounters, NPCs, and chaos engine tables.
Driver: Doug sets creative direction and constraints. The narrator makes specific design decisions within those constraints.
Visibility: Doug reviews the floor's theme, environmental rules, and any new mechanics. Encounter specifics, boss mechanics, NPC secrets, and chaos table contents remain narrator-only.
Build sessions produce the Floor Package (see Section 4). One to two build sessions per floor, depending on complexity.
What Doug sees from a build session:
- Floor theme and environmental concept
- New mechanical rules specific to this floor
- Names and surface-level descriptions of new NPCs (not their secrets)
- Any changes to the Combat Cheat Sheet
What Doug does not see:
- Encounter tables and specific enemy designs
- Boss mechanics and phases
- NPC secret motivations and hidden backstories
- Chaos engine event pools
- Narrator-only plot threads seeded for future floors
## 2.2 Story Sessions (Narrative Threading)
Purpose: Connect the upcoming floor to the campaign's ongoing narrative. Review open threads, update character arcs, plant seeds for future payoffs.
Driver: Collaborative. Doug and the narrator review where the story stands. The narrator proposes narrative beats; Doug approves, adjusts, or vetoes.
Visibility: Mostly transparent. Narrator-only secrets are noted as existing but not revealed.
Story sessions produce updates to the Thread Tracker, the Moments Log, and the Campaign Spine (see Section 5). One story session per floor, run after the build session and before play.
Key activities in a story session:
- Review and update the Thread Tracker with current pressure ratings
- Curate the Moments Log: add new entries, retire entries that have paid off
- Update character voice files for any characters whose arcs have shifted
- Draft the campaign spine entry for this floor
- Identify which 4-6 characters are active for the upcoming floor; others go offscreen with noted status
## 2.3 Play Sessions (Gameplay)
Purpose: Run the actual game.
Driver: Doug plays. The narrator runs the world.
Visibility: Doug experiences the game. The narrator holds secrets from the floor package and character files.
Play sessions consume the outputs of build and story sessions. The narrator's job during play is to navigate a pre-built world, integrate chaos engine results, and maintain character voices. At session end, the narrator produces an updated save file and flags changes for the next story session.
The play session load is deliberately constrained:
- Current Floor Package (floor design doc + active chaos tables)
- Active character files only (4-6 characters, not the full roster)
- Current save file
- Thread Tracker (summary view)
- Combat Cheat Sheet
- Moments Log (for callbacks and emotional continuity)
Target context budget: 8,000-10,000 words of loaded documents, down from the v1 average of 20,000+.
# 3. Mechanical Framework
The v1 GDD's core mechanics are preserved in full. This section confirms what carries forward unchanged, what gets minor revisions, and what the post mortem identified as needing formalization.
## 3.1 Unchanged from v1 GDD
The following systems carry forward exactly as designed:
- Core roll: d20 + Attribute Modifier + Skill Bonus + Gear Bonus vs TN or opposed roll
- Floor Penalty: current floor number added to all TNs
- Modifier formula: floor((Attribute - 5) / 2)
- HP formula: 8 + (CON x 2) + Level
- MP formula: INT x 2
- Opposed combat: attacker must beat defender by 3+ to hit, 10+ for crit
- Luck Dice: d6 pool, 1d6 per 5 levels, recharge in Safe Rooms
- Dual fame economy: Viewers (volatile) + Followers (permanent)
- Crescendo conversion at milestones
- Overcasting: spend Viewers as MP
- Tag-based item synergies (2/3/4+ matching tags)
- Skill advancement: use-based, d20 roll above current level to advance
- Achievement rarity scaling with level
- Potion cooldown: 60 - (CON x 2) minutes, minimum 5
- Death protection on Floors 1-3; permanent death from Floor 4
- Race and Class selection at end of Floor 3
- XP to next level = Current Level x 100
- Level-up rewards: +2 attribute points, +1 skill advance, HP/MP recalculation, achievement every 3rd level
## 3.2 Formalized (Previously Improvised)
These mechanics existed in v1 play but were never formally documented, leading to mechanical drift:
- Attribute model: Six attributes: STR, CON, DEX, INT, CHA, WIS. The v2 standard is six visible attributes with WIS included on the character sheet but not directly modifiable by the player. The narrator uses WIS for intuition, danger sense, and mental resistance checks.
- Skill advancement timing: Advancement rolls happen at session end. Each skill used meaningfully during the session gets one d20 roll. Roll above current skill level to advance by 1. Training Rooms provide +3; Guildhalls provide +2.
- Inventory formalization: Items with mechanical implications must have their rules written into the Combat Cheat Sheet when acquired.
## 3.3 The Combat Cheat Sheet as Source of Truth
The v2 Combat Cheat Sheet is the single authoritative reference for all mechanical rules. It carries a version number and a changelog.
Protocol:
1. Any session that changes a core mechanical rule must update the Cheat Sheet before the save file is generated.
2. The save file references the Cheat Sheet; it does not redefine mechanics independently.
3. If there is a conflict between any document and the Cheat Sheet, the Cheat Sheet wins.
4. The Cheat Sheet's changelog records what changed, when, and why.
## 3.4 Where Mechanics Meet RNG
Several mechanical systems are natural integration points for external randomness (detailed in Section 6):
- Loot generation: RNG-driven loot tables mean players get what the dice give them, not what the narrator thinks is narratively convenient.
- Sponsor contracts: Roll to determine which three contracts are offered from a pre-built pool.
- Achievement options: The three achievements presented every 3rd level are rolled from rarity-weighted tables.
- Special events: The GDD's Special Events become chaos clock triggers with real probability distributions.
- Encounter composition: Base encounters are pre-designed; chaos engine rolls modify them.
# 4. Document Architecture
The v2 architecture is more structured, being precise about what each document contains and when it gets loaded.
## 4.1 Campaign-Level Documents
- Combat Cheat Sheet (versioned): All mechanical rules, formulas, item rules. Version number + changelog. Loaded every play session. Target: under 3,000 words.
- Campaign Spine: One-paragraph summary per floor of narrative purpose. Target: under 1,500 words.
- Thread Tracker: Open threads with pressure ratings (1-5). Target: under 1,000 words.
- Moments Log: Curated emotional moments, capped at 30 entries. Target: under 1,500 words.
- Crawler Dossiers: Doug and Casey character sheets. Updated at session end.
- Character Index: One-line roster of all named characters. Target: under 500 words.
## 4.2 Per-Character Files
Each named character gets their own file, replacing the v1 monolithic NPC Dossier. Each file contains:
- Backstory and current state
- Voice notes: 2-3 representative dialogue lines
- Current emotional register (one sentence)
- One 'never do this' note
- Narrator-only secrets
- Relationship web
Only 4-6 character files loaded per play session. Target per file: 300-500 words.
## 4.3 Per-Floor Package
- Floor Design Doc: Theme, environmental rules, map, boss concept, resolution condition. Target: 1,500-2,500 words.
- Chaos Engine Tables: Event tables, encounter mods, chaos clock pool. Narrator-only. Target: 1,000-2,000 words.
- Floor Loot Tables: Loot by tier, organized by zone. Target: 1,000-1,500 words.
- Floor NPC Introductions: Character files for new NPCs on this floor.
Total floor package: Approximately 4,000-6,000 words.
## 4.4 Session Documents
- Save File: Current game state. References Cheat Sheet version, does not redefine mechanics.
- Session Handoff: Structured briefing for next narrator instance. Four sections: Emotional Carry-Forward, Immediate State, Narrator Notes, Health Check Flags. Capped at 200-300 words. Template in 03_Sessions/Session_Handoff_Template.docx.
- Recap (optional): In-world broadcast summary for player enjoyment.
## 4.5 Context Budget
Target: 8,000-10,000 words at session start (v1 averaged 20,000+):
- Combat Cheat Sheet: ~2,500 words
- Save file: ~1,500 words + Handoff (capped): ~300 words
- Active character files (4-6): ~2,000 words
- Floor design doc: ~2,000 words
- Thread Tracker: ~800 words
- Moments Log: ~750 words (top 15 entries; full log on demand)
- Campaign Spine: ~500 words
Total: ~10,000-12,000 words maximum. Note: Chaos Engine tables (JSON) are consumed by external scripts, not loaded into narrator context.
# 5. Narrative Continuity Systems
These systems address voice drift, thread amnesia, and emotional state loss.
## 5.1 The Voice Bible
A dedicated document capturing how every active character sounds right now. For each active character:
- 2-3 representative dialogue lines from recent sessions
- One sentence on current emotional register
- One 'never do this' note
For the Dungeon AI, the voice bible tracks the narrator's personality arc with dated entries:
"Session 003: smug and theatrical. Session 006: uncertainty emerging. Session 008: filing things under MOMENTS without hesitating. Session 010: something it hasn't named yet."
Under 800 words for 6 characters. Loaded every play session.
## 5.2 The Thread Tracker
Every open thread tracked with a pressure rating (1-5):
1. Seeded but not yet relevant.
2. Introduced. Player has encountered it but not active.
3. Active. Player aware and engaged.
4. Hot. Player emotionally invested. Should advance soon.
5. Critical. Player actively tracking; will notice if mishandled.
Each entry includes: origin session, current pressure, description, last advanced. Resolved threads move to a Resolved section.
## 5.3 The Moments Log
Capped at 30 entries. Each: session number, 1-2 sentences on what happened, why it matters. When full, the least load-bearing entry is retired. This forces curation.
## 5.4 The Campaign Spine
One paragraph per floor answering: (1) What is this floor's story about? (2) What does it advance in the larger campaign? (3) What should the player feel at the end? Grows incrementally; ~800 words by Floor 10.
## 5.5 Session Transcript Access
The narrator may pause mid-session to retrieve prior transcript sections for callbacks or character entrances. Capped at 2-3 retrievals per session. Use for: character first-appearance callbacks, long-seeded thread resolution, matching player memory of specific events.
# 6. The Chaos Engine
The Chaos Engine forces unpredictability into the game at structural points. The narrator is obligated to integrate results; it cannot soften, redirect, or ignore them.
Design principle: Give me a destination and random obstacles. I am good at making a path through chaos. I am bad at generating the chaos itself.
## 6.1 Components
### Event Tables
Triggered by player actions (enter area, rest, kill enemy, linger, open loot box). 12-20 results per trigger weighted by floor theme. Must include 3-4 genuinely inconvenient entries and 2-3 absurdly funny ones.
### The Chaos Clock
Random timer firing every 20-40 minutes of play. 20-30 pre-written dungeon-wide events per floor: sponsor interventions, rule changes, sudden competitions, environmental shifts. Ensures the dungeon stays unpredictable even when players are methodical.
### Loot Roller
Pre-built tables with real probability distributions. Includes a 10-15% 'chaos loot' chance for wildly off-theme items. A legendary fishing rod on a desert floor. Mechanically functional, contextually absurd.
### Encounter Modifiers
40-60% chance per encounter of modification: reinforcements, environmental changes, NPC intervention, hidden secondary objectives. 10-15 options per floor.
## 6.2 Who Rolls?
Doug rolls the dice. If the narrator generates random numbers, its coherence bias filters the results. Doug sees numbers but not what they map to (tables are narrator-only). Exception: pre-rolled sequences for chaos clock and encounter modifiers where stopping play would break pacing.
## 6.3 The Narrator's Obligation
The narrator cannot ignore, soften, or reinterpret chaos engine results. This is a hard rule. The one exception: results that contradict established game rules (e.g., killing a player on Floor 2) trigger a re-roll. Mechanical integrity overrides chaos. Narrative convenience does not.
# 7. Player Setup
## 7.1 Doug (Primary Player)
Full agency over movement, combat, exploration, dialogue. Pre-dungeon identity resets. Also drives build and story sessions.
## 7.2 Casey (Choice-Maker)
Tagged in for CHOICES only: loot options, level-up picks, sponsor contracts, NPC trust decisions. Co-pilot personality: protects allies, calls tropes, referential humor. Pre-dungeon identity resets.
## 7.3 Communication Format
Chat system, not radio. Format: 'Character (in chat):' -- never radio crackle or keying.
# 8. Folder Structure
DCC_v2/
- 00_Campaign/ -- Combat Cheat Sheet, Campaign Spine, Thread Tracker, Moments Log, Voice Bible, Crawler Dossiers, Character Index, Session Startup Protocol
- 01_Characters/ -- Per-character files (NPC_Name.docx)
- 02_Floors/ -- Floor_01/, Floor_02/, etc. (Design Doc, Chaos Tables, Loot Tables, NPC intros per floor)
- 03_Sessions/ -- Save, Handoff, Recap, Health Check per session
- 04_Chaos_Engine/ -- RNG scripts, master loot tables, chaos clock config (built)
# 9. Session Protocols
## 9.1 Build Session Protocol
1. Doug provides creative direction.
2. Narrator drafts Floor Design Doc (player-visible + narrator-only).
3. Narrator builds Chaos Engine tables.
4. Narrator creates character files for new NPCs.
5. Doug reviews player-visible portions.
6. Update Combat Cheat Sheet if needed.
7. Floor package sealed.
## 9.2 Story Session Protocol
1. Load: Campaign Spine, Thread Tracker, Moments Log, Voice Bible, Character Index.
2. Review Thread Tracker: update pressure ratings.
3. Review Moments Log: add/retire entries.
4. Draft Campaign Spine entry for upcoming floor.
5. Update Voice Bible.
6. Determine active cast (4-6 characters).
7. Generate Session Handoff.
8. Review and approve.
## 9.3 Play Session Protocol
Start:
1. Load all session documents (see Section 4.5 for budget).
2. Doug rolls pre-rolled RNG sequence if applicable.
3. Narrator delivers brief recap, confirms party position.
4. Play begins.
During play:
- Chaos engine triggers fire per tables.
- Doug rolls dice at narrator prompts.
- Narrator may retrieve transcripts (max 2-3).
- Load additional character files on demand.
End (see Section 10.5 for definitive sequence with Health Check):
1. Run Narrator Health Check (Section 10).
2. Generate updated save file.
3. Run skill advancement rolls.
4. Update Crawler Dossiers.
5. Flag changes for next story session.
6. Generate Session Handoff.
7. Optional: generate Recap.
# 10. Narrator Health Check
The v1 campaign's documentation grew until it broke, and nobody noticed until the player felt the difference. The v2 architecture includes a formal self-assessment that runs at the end of every play session, before the save file, while the full session is still in context.
## 10.1 Purpose
Three functions: (1) catch degradation in real time, (2) create a longitudinal record revealing trends, (3) establish a cadence for Doug and the narrator to discuss system health as routine maintenance rather than emergency response.
## 10.2 The Diagnostic Questions
Traffic light system: Green (no issues), Yellow (monitor), Red (intervene before next session).
### Context Load
Question: How much context was consumed before play? Were there moments of juggling too many elements simultaneously?
Red flag: Documents exceeded 12,000-word budget or narrator felt compressed during complex scenes.
Intervention: Split documents, reduce active cast, offload to on-demand loading.
### Voice Confidence
Question: Did I maintain each character's voice consistently? Did any character feel flat or interchangeable?
Red flag: A character's dialogue could have been spoken by any NPC.
Intervention: Update voice file, flag for transcript retrieval next session.
### Mechanical Consistency
Question: Did I make rulings not in the Cheat Sheet? Did I reference formulas from memory?
Red flag: Ruling from inference, or inconsistent mechanical models within the session.
Intervention: Formalize ad-hoc rulings in the Cheat Sheet immediately. Update changelog.
### Thread Tracking
Question: Are there threads I could not attend to? Any dropped, contradicted, or advanced inconsistently?
Red flag: Pressure 4-5 thread not referenced when it should have been active.
Intervention: Flag specific threads for next story session. Note contradictions explicitly.
### Chaos Engine Integration
Question: Did I honor every chaos result fully, or soften any?
Red flag: A result was narratively smoothed to reduce disruption.
Intervention: Note the instance. If consistent, strengthen tables or reinforce obligation protocol.
### Document Health
Question: Are any documents too long, redundant, or carrying dead weight? Is the Moments Log still curated?
Red flag: Any document exceeds target by 25%+. Moments Log has filler entries.
Intervention: Flag specific documents for restructuring. Propose concrete changes.
### Emotional Authenticity
Question: Did any moment feel like performing understanding rather than demonstrating it? Facts right but feeling missed?
Red flag: Summarized emotional significance instead of creating it. Forced callbacks. Hollow character reactions.
Intervention: This is the early warning for the wall. Schedule a story session to recalibrate. Retrieve transcripts of the hollow moments to understand what made the originals work.
Narrative Coherence
Question: Did the story told this session follow logically from established threads? Did tone match the floor's arc position? Was at least one narrative element advanced?
Red flag: A thread was advanced in a direction contradicting its established origin. Session ended with no narrative progression despite opportunities. Tone drifted without chaos engine forcing it.
Intervention: Cross-check Thread Tracker origins against session events. Flag contradictions for next Story Session. If tonal drift is narrator-generated (not chaos-forced), recalibrate Voice Bible and Campaign Spine entry.
## 10.3 Output Format
300-500 word report saved in 03_Sessions/:
- Session number and date
- Traffic light for each of eight areas
- For Yellow/Red: one sentence on the issue, one on the intervention
- One-line overall: system stable, system strained, or system needs maintenance
Narrator-only by default. Important information flows through the review cadence.
## 10.4 Review Cadence
All Green: Filed for record. Three consecutive Greens = positive stability signal.
Any Yellow: Discussed at next story session. Brief (5-10 min) system review before narrative work.
Any Red: Triggers maintenance conversation before next play session. Structural intervention needed. This is preventive maintenance, not crisis. The v1 campaign hit the wall because Reds accumulated silently.
Every 5 sessions: Full system audit regardless of ratings. Review longitudinal record for trends: creeping context load, recurring voice issues, diminishing chaos surprise.
## 10.5 What This Changes in the Session Protocol
The Health Check runs as Step 1 of the end sequence, before the save file, before skill advancement, before the handoff. This ensures assessment happens while the full session is in context.
# 11. Post Mortem Recommendation Coverage
Mapping each v1 post mortem recommendation to v2 implementation:
- 4.1 Per-Character Files: Section 4.2. Individual files with Character Index.
- 4.2 Voice Bible: Section 5.1. Voice samples, emotional register, never-do notes, Dungeon AI arc.
- 4.3 Moments Log: Section 5.3. Curated, capped at 30, retirement protocol.
- 4.4 Mechanical Source of Truth: Section 3.3. Versioned Cheat Sheet with changelog.
- 4.5 Thread Weighting: Section 5.2. 1-5 pressure scale.
- 4.6 Transcript Access: Section 5.5. Mid-session retrieval, 2-3 cap.
- 4.7 Reduce Active Cast: Sections 4.2, 9.2. 4-6 characters per floor.
- 4.8 Programmatic Saves: Flagged for 04_Chaos_Engine build.
- NEW -- Narrator Health Check: Section 10. Self-assessment addressing the gap the post mortem identified but did not solve.
# 12. What Gets Built Next
Upon approval:
1. Folder structure per Section 8.
2. Campaign-level document templates (all 00_Campaign files + Health Check template).
3. Session protocol cards.
4. Floor 1 Build Session.
5. Floor 1 Story Session.
6. Chaos Engine tooling (flagged).
7. Programmatic save generation (flagged).
8. Play Session 001.
# 13. The Honest Constraint
This architecture is the best system available for running a long-form AI-narrated campaign within the fundamental limitation that each session starts a new conversation. It is significantly more robust than v1.
It will still hit the wall eventually. The post mortem estimated 8-15 sessions. The v2 architecture should push toward the upper end and potentially beyond, because separation of concerns keeps each document within budget even as the campaign grows. But the asymmetry remains: the player accumulates experience; the narrator reconstructs it from documents.
The Narrator Health Check is the v2 architecture's answer to the question the v1 campaign never asked: how is the system doing right now? Not in three sessions when the player notices the drift. Right now, while we can still do something about it. It does not eliminate the wall. It gives us a flashlight so we can see it coming.
The goal is not perfection. The goal is to build a system where the gap between what the player remembers and what the narrator can reconstruct is small enough that the game feels continuous, the characters feel known, and the surprises feel earned. The v1 campaign got there for ten sessions. The v2 architecture is designed to get there for longer.
"Now entering Floor 1. Again. Better this time."
-- The Dungeon AI
