"""
DCC v2 — Context Checkpoint System
Tracks session duration and exchange count. Provides proactive integrity checks
to catch context degradation before it affects play quality.

The narrator runs this system during play. It does NOT replace the end-of-session
Health Check — it catches problems mid-session so we can save before quality drops.

Usage (integrated into play session, not run standalone):
  From within a session, the narrator mentally tracks exchanges and time.
  When a checkpoint fires, the narrator runs the self-check and reports the signal.

  This script provides the protocol definition and can generate checkpoint
  reminder cards for session prep.

Standalone usage for session prep:
  python context_checkpoint.py prep [--session-length 180]
  python context_checkpoint.py protocol
"""

import argparse
import random

# ============================================================
# CHECKPOINT PROTOCOL
# ============================================================

PROTOCOL = """
CONTEXT CHECKPOINT PROTOCOL
============================

WHEN TO CHECK:
  - Every 45-60 minutes of play time, OR
  - Every 15-20 narrator-player exchanges, OR
  - Whenever the narrator feels uncertain about a detail it should know

  Whichever comes first. If unsure, check. False alarms cost nothing.
  Missed degradation costs a session.

THE SELF-CHECK (5 questions, ~30 seconds):

  1. VOICE TEST
     Can I produce a distinctive line of dialogue for each active character
     right now — not a summary of how they talk, but an actual line?
     PASS: Yes, and they sound different from each other.
     FAIL: A character's voice feels generic or interchangeable.

  2. MECHANICAL RECALL
     Can I cite the exact formula for the last mechanical ruling I made
     (HP calculation, damage roll, skill check TN) without re-reading
     the Cheat Sheet?
     PASS: Yes, I can state the formula.
     FAIL: I'm reconstructing from inference, not recall.

  3. THREAD AWARENESS
     Can I name the top 3 threads by pressure rating and their current state?
     PASS: Yes, with specifics.
     FAIL: I'm guessing or conflating threads.

  4. POSITION CLARITY
     Do I know exactly where every active party member and NPC is right now,
     what they're doing, and what they want?
     PASS: Yes, I can state each character's physical and emotional position.
     FAIL: I've lost track of someone or I'm assuming positions.

  5. CONTINUITY CHECK
     Does what just happened in the last 2-3 exchanges follow logically from
     what happened 10-15 exchanges ago? Am I maintaining cause and effect?
     PASS: Yes, the story is internally consistent.
     FAIL: I've introduced something that doesn't follow, or I've forgotten
           a consequence that should be in play.

SCORING:
  5/5 PASS → STABLE. Continue play. Next checkpoint in 45-60 min.
  3-4/5 PASS → STRAINED. Wrap current scene within 15-20 minutes.
                Flag which checks failed. Consider transcript retrieval
                for the weak areas. Save at end of current scene.
  0-2/5 PASS → SAVE NOW. Stop play gracefully at the next natural pause.
                Execute end-of-session sequence immediately. Do not push
                through — the quality debt compounds from here.

OUTPUT FORMAT (inline during play):
  [Checkpoint: STABLE — all checks pass. Next checkpoint at ~{time}.]
  [Checkpoint: STRAINED — voice test and thread awareness fuzzy. Wrapping scene.]
  [Checkpoint: SAVE NOW — mechanical recall and continuity failing. Saving.]

THE NARRATOR'S OBLIGATION:
  The narrator cannot skip, delay, or downplay a checkpoint result.
  STRAINED means strained. SAVE NOW means save now.
  This is the same hard rule as chaos engine integration:
  narrative convenience does not override system integrity.

RELATIONSHIP TO HEALTH CHECK:
  Checkpoints are mid-session early warning.
  The Health Check is end-of-session comprehensive review.
  If a checkpoint triggers STRAINED or SAVE NOW, the Health Check MUST
  reference it under Context Load — it's a data point for the longitudinal
  record. Don't re-assess from scratch; build on what the checkpoint found.
"""

# ============================================================
# SESSION PREP: Generate checkpoint schedule
# ============================================================

def generate_checkpoint_schedule(session_length_minutes: int = 180) -> list[dict]:
    """
    Generate a suggested checkpoint schedule for a session.
    Checkpoints are spaced 45-60 minutes apart with some randomness.
    """
    checkpoints = []
    current = random.randint(45, 60)
    checkpoint_num = 1

    while current <= session_length_minutes:
        checkpoints.append({
            "number": checkpoint_num,
            "time_minutes": current,
            "time_display": f"{current // 60}h{current % 60:02d}m" if current >= 60 else f"{current}m",
            "exchange_estimate": checkpoint_num * 17,  # ~17 exchanges per checkpoint
        })
        checkpoint_num += 1
        current += random.randint(45, 60)

    return checkpoints


def print_prep_card(session_length: int = 180):
    """Print a checkpoint prep card for the narrator."""
    schedule = generate_checkpoint_schedule(session_length)

    print("=" * 50)
    print("  CONTEXT CHECKPOINT — SESSION PREP CARD")
    print("=" * 50)
    print(f"  Session length: {session_length} minutes")
    print(f"  Checkpoints scheduled: {len(schedule)}")
    print()

    for cp in schedule:
        print(f"  Checkpoint #{cp['number']}: {cp['time_display']} (~exchange {cp['exchange_estimate']})")

    print()
    print("  At each checkpoint, run the 5-question self-check.")
    print("  STABLE → continue. STRAINED → wrap scene. SAVE NOW → save immediately.")
    print()
    print("  Remember: exchange count is a backup trigger.")
    print("  If you hit 15-20 exchanges before the next time checkpoint,")
    print("  run the check anyway.")
    print("=" * 50)


def print_protocol():
    """Print the full protocol for reference."""
    print(PROTOCOL)


def main():
    parser = argparse.ArgumentParser(description="DCC v2 Context Checkpoint System")
    parser.add_argument("mode", choices=["prep", "protocol"], help="'prep' for session prep card, 'protocol' for full protocol")
    parser.add_argument("--session-length", type=int, default=180, help="Session length in minutes (default: 180)")

    args = parser.parse_args()

    if args.mode == "prep":
        print_prep_card(args.session_length)
    elif args.mode == "protocol":
        print_protocol()


if __name__ == "__main__":
    main()
