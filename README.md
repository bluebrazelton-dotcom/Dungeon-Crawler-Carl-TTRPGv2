# Dungeon Crawler Carl — The Game (v2)

A custom tabletop RPG campaign, built and run in collaboration with an AI narrator.

This repository is the complete production state of an 18-floor TTRPG campaign inspired by Matt Dinniman's *Dungeon Crawler Carl*. It is also a deliberate experiment in **human–AI collaborative design**: a record of what it takes to make an AI narrator run a mechanically complex, emotionally coherent role-playing game across many sessions without losing the thread.

> Note on names: player references in these documents use the alias **Doug**.

## What this is

The project began as v1 — proof that an AI narrator *could* run a complex TTRPG across multiple sessions. It worked, and then it broke at scale. A post-mortem identified five recurring failure modes: voice drift, mechanical drift, thread amnesia, contextual compression, and emotional-state loss. All five trace to one root cause: each session starts a fresh conversation with no persistent memory.

**v2 is the rebuild.** It doesn't pretend to fix the memory constraint — it restructures the entire campaign to work *within* it. Three principles drive every design decision:

- **Separate what changes from what persists.** Stable mechanics live in versioned reference documents loaded every session. Cumulative narrative lives in structured logs that grow over time. Volatile creativity lives in pre-built floor packages.
- **Take randomness out of the narrator's hands.** An AI narrator is biased toward narrative coherence; DCC's identity is chaos that characters make meaning from. External RNG systems (the Chaos Engine) force the narrator to integrate results it would never have invented.
- **Build the world before you play in it.** World-building, storytelling, and gameplay are split into distinct session types, so the narrator arrives at each play session with a world to navigate rather than an empty room to improvise.

## The three-session framework

Every floor is produced through three session types, run in order:

1. **Build sessions** — design the floor's space, mechanics, encounters, NPCs, and Chaos Engine tables. The player sets direction and constraints; the narrator makes design decisions within them.
2. **Story sessions** — review where the narrative stands, surface open threads, and set up payoffs. Collaborative.
3. **Play sessions** — run the actual game. The player plays; the narrator runs the world; external RNG decides chaos.

## Repository structure

```
DCC_v2/
├── DCC_v2_Architecture_Blueprint.docx   Complete system design (reference)
├── Master_File_Index.docx               Table of contents — what to load when
├── Floor_1_Build_Handoff.docx           Per-floor build/story handoffs
├── Floor_2_Build_Handoff.docx
├── 00_Campaign/      Persistent docs: mechanics, voice bible, spine, trackers, protocols
├── 01_Characters/    Crawler and NPC sheets
├── 02_Floors/        Built floor packages (Floor_01, Floor_02, ...)
├── 03_Sessions/      Session saves and recaps
├── 04_Chaos_Engine/  Python tooling for external randomness + table format
└── 05_Snapshots/     Point-in-time backups of campaign state per session
```

Most documents are Word files (`.docx`) because that's the working format of the campaign. Key structural and narrative documents also have a Markdown companion (`.md`) alongside them, so the project is readable on GitHub and so meaningful edits show up in the commit history as legible diffs.

## The Chaos Engine

`04_Chaos_Engine/` holds the Python that generates external randomness — the mechanism that keeps the narrator honest. Rather than letting the AI invent "random" outcomes (which trend toward tidy storytelling), the engine rolls against pre-built tables and hands the narrator results it has to make meaning from. `TABLE_FORMAT.md` documents the table schema; `floor_XX_tables.json.example` is a template.

## On the AI collaboration

This repo is partly a portfolio artifact: evidence of a real, sustained project built *with* AI rather than *by* a single prompt. The architecture blueprint, post-mortem, and session protocols document the workflow itself — how creative direction, system design, and live play were divided between a human author and an AI narrator, and how the system was iterated when it failed.

## Credits

Built by **Doug** in collaboration with an AI narrator. Inspired by the *Dungeon Crawler Carl* series by Matt Dinniman. This is a non-commercial fan project for personal play.
