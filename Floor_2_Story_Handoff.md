# FLOOR 2 STORY SESSION — HANDOFF
From: Floor 2 Build Session (May 23, 2026)
To: Floor 2 Story Session → Floor 2 Session 001 Play
# What Was Done
Floor 2 design is locked. Full design doc, loot tables, and chaos engine JSON exist in 02_Floors/Floor_02/. Build_Handoff exists in DCC_v2/ root. This file is the Story Session companion — it articulates the narrative shape Floor 2 should take across its 4-6 sessions of play, the emotional arc, the order of NPC introductions, and the specific scenes the narrator should be ready to land.
Floor 2's design philosophy in one sentence: where Floor 1 was a place that knew it was ending and did customer service anyway, Floor 2 is a place that does customer service forever and isn't sure anyone notices.
# Floor 2 Narrative Shape
## Session 1 (estimated): Arrival & Onboarding
Crawlers descend the Floor 1 stairwell. The transition is jarring — Floor 1's PA voice (Penny, now) wishes them well over the speaker; the moment they cross the threshold, the audio cuts to corporate hold music. They emerge into the Onboarding Room.
Angie's onboarding video plays. She is reading off cue cards. Her voice is rehearsed. Players will notice. She introduces them to: their cubicle assignments, the Call Queue, the headsets, the CSAT system. The video ends with: 'Have a great first day. Team meeting is at 9, every day, forever.'
First call (E2): GalacticBrew on the line, asking about Pennybrook's data delays. Players resolve via CHA. CSAT lands for the first time. Players have a number now.
End of session: players have met Marcus (briefly, in the break room — he nods) and have closed at least 2 calls. Performance Tokens awarded. PHRYNE feed introduced.
## Session 2: The Floor Supervisor's Wing
Zone B opens. Angie's coaching scene. She is professional, helpful, slightly tired. She does not say what she has done. She gives Doug and Casey actual coaching feedback that improves their mechanical CSAT performance.
First sponsor contract pitched (chaos clock fires Halcyon Headsets or PHRYNE Pro depending on roll). Players choose 0-2.
First glimpse of the Wall of Champions. Casey, with the genre-awareness instinct, should notice the pattern of names. The narrator should let her work it out.
Janine is introduced in this session. She runs them through their first training scenario. Bright, energetic, brittle. Players will probably like her.
## Session 3: The Break Room & the Quiet Room
Zone C opens. Players find the break room. They meet Vincent for the first time. The narrator does not name him as fake. The mug is full when looked at, empty when set down. Casey notices.
Marcus is in the break room. He nods. He's reading. If Doug strikes up a conversation, Marcus is willing to talk. If Doug asks Marcus about himself, Marcus says he's been on a long shift. (Truth: he died in 2019.)
The Quiet Room door appears at the end of the hallway. The narrator lands the silence. Players have to decide whether to investigate.
Tasha's mother voicemail hits the hold music for the first time during a routine call. Players who notice: they will demand the file. The path to retrieving it requires the Quiet Room.
End of session: the Quiet Room is on the table. At least one Crawler should be tempted to enter it before Session 4.
## Session 4: The Server Farm & the Quiet Room
Two parallel pressures. Zone D opens — Keys is in the server farm. He DM's whichever Crawler hit the highest INT. He shows them the floor's infrastructure layer. He shows them the Legacy System (E7). He offers a path to causing real trouble.
Meanwhile: the Quiet Room. If a Crawler enters and answers the personal call, the narrator lands the call. Doug's caller (default): Sue. Reason: Floor 1 established Sue as Doug's grounding figure. Casey's caller: TBD — see Open Questions. The call is 30 minutes (real time, or 1 scene). Players hang up or stay on. Reward: Quiet Room item + permanent +1 WIS.
If the players retrieve Tasha's mother voicemail (via Quiet Room route — narrator-mediated): they now carry it. What they do with it is Floor 3+ optional content.
End of session: at least one CSAT threshold crossed (Top Performer or above for at least one Crawler). Escalation route is approaching.
## Session 5-6: The Escalation
The Escalation door manifests. Players walk in. Charles is at his desk. He greets them politely. The fight is optional.
Phase 1 (145 -> 70 HP): The 'we should talk' branch opens automatically if CSAT is 4.0+. Otherwise, combat with lair actions (rolled on escalation_lair in JSON).
Phase 2 (70 -> 0 HP): Charles loosens his tie. His real voice. He has been doing this for 39 years. He would like to retire. CHA opposed contest, TN 18. Win: Charles stands down, hands the nameplate, optionally The Black Binder. Lose: bitter fight, +3 to his rolls, permanent death possible on his next crit.
Closing the floor: the stairwell opens. The Reps look up. PHRYNE final message from @KEYS. The Crawlers descend.
# Load These Documents (per protocol)
Follow the Play Session Protocol in 00_Campaign/Play_Session_Protocol.docx for each session.
Always load before a Floor 2 session:
- Master_File_Index.docx
- 02_Floors/Floor_02/Floor_02_Design_Doc.docx
- 02_Floors/Floor_02/Floor_02_Loot_Tables.docx
- 02_Floors/Floor_02/floor_02_tables.json (via chaos_engine.py)
- 00_Campaign/Combat_Cheat_Sheet.docx (v1.3+)
- 00_Campaign/Voice_Bible.docx (Floor 2 supplement)
- 00_Campaign/Thread_Tracker.docx
- 00_Campaign/Crawler_Dossiers.docx
- 01_Characters/Floor_02/ — all 5 NPC files
- Previous session's Save file and Handoff (for context continuity)
# Deliverables for This Session
- Story Session beat plan finalized — confirm or revise the Session 1-6 outline above
- Casey's personal call content — who calls her in the Quiet Room (must be planted before Session 4)
- Doug's secret equipped item [REDACTED] — does it interact with the call center? (Narrator does not know what it is — but the floor's listening mechanic may give Doug an opportunity to use it. Story Session should not pry; just leave room.)
- 12 PHRYNE seed messages (Voice Bible) — sample range: work jokes, gossip, complaint threads, Wall of Champions chatter, Marcus moderation, Keys IT shitposts, Angie absence noticed
- 3 voice samples per named NPC (Angie, Marcus, Janine, Keys) — locked tone signatures
- Charles's Phase 1 and Phase 2 voice samples (3 each) — locked tone shift
- Combat Cheat Sheet v1.3 — CSAT rules, PT rules, permanent death clarifications, Compliance Action codification
# Prerequisite — Decide Before Story Session Closes
- Casey's Quiet Room caller. Possible options: Casey's grandmother (if Doug/narrator wants direct emotional weight), a former bandmate (lighter, regret-tinged), an unnamed someone Casey didn't get to say goodbye to (most flexible — Story Session can keep the identity tacit). The narrator MUST plant the identity in Story Session because the call is the floor's emotional payoff for Casey.
- How aggressive should the floor be about Vincent? If Casey clocks the pattern in Session 3, does the narrator confirm or play coy? Recommendation: play coy. Let the table sit with the wrongness across Session 3-4. Only confirm if pressed directly with a CHA roll against the Reps.
- Should Tasha's mother voicemail be retrievable on Floor 2, or only audible in hold music? Default plan: retrievable via Quiet Room route. Decide if the narrator wants to make it harder (require also a PHRYNE leak action or a Keys infrastructure unlock).
# Key Things to Flag
- Permanent death is on. Doug must know this. The narrator should land this clearly at the floor entry PA broadcast and reinforce it in Marcus's first coaching scene if applicable.
- Floor 1 carry items: Doug and Casey still have Snake Canes, Tasha's Mall Keychain, Sal's Lighter, Dana's Socks, Sal's Farewell Pizza (4 slices), Unit 7 Frosting Recipe, Badge #1 Maglite (Doug), Badge #1 Cap (Casey), the Rare Garland lanyard (Doug), the Pennybrook radio. The Mall-tagged items lose their mall-NPC bonus on Floor 2 — but they may pick up new flavor on PHRYNE (Reps noticing the merchandise).
- Doug's [REDACTED] secret item: honor the secret. The narrator does not know what it is. Leave moments for Doug to deploy it.
- Casey's role: co-pilot. She tags for loot choices, level-up choices, sponsor decisions, and trust calls. She does NOT direct combat or RP for Doug. She CAN take the personal call in the Quiet Room — that is a Casey-specific scene.
# Rules That Carry Forward
- Voice Bible compliance is a per-session check. Marcus heard everything in his prior life and will catch dialogue drift if it happens — use Marcus as a meta-check: if the narrator suspects voice drift, write Marcus into a scene to coach.
- Snapshot every Play Session via snapshot.py.
- Health Check at end of every session — log Mechanical, Document, Narrative, Chaos Engine status. Carry forward YELLOWs explicitly.
- Context Checkpoints every 30-40 minutes of play. Save file generated end of each session.
- Chaos Engine consultation is non-negotiable. The narrator does not skip rolls because the table is going well. The clock fires when the clock fires.
# Open Questions for Story Session to Resolve
- Does Vincent's reveal — if it happens — carry into Floor 3+? Recommended: yes; Vincent's grief can attach to another character mode on Floor 3+ if the players took the time to engage.
- Does Keys's infrastructure thread carry forward? If the players befriend Keys, does he reappear (via PHRYNE message, via descent assistance, via cameo on Floor 5)? Recommended: yes; Keys is the kind of character Doug will remember.
- Sponsor contract conflict resolution — if Doug takes Halcyon and Quietude, the two sponsors will conflict (Halcyon listens to calls; Quietude rewards silence). Story Session should pre-plan the conflict scene.
- How visible should the dead Reps be? Marcus is dead and doesn't know. There are likely others. How many Reps on the floor are dead? Recommended: don't quantify it; let the question linger as Floor 2's central horror.
The floor listens. The narrator should listen back. Build the Story Session as you would a coaching scene — Floor 2 will hear the difference.
