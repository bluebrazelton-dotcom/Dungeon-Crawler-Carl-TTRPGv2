"""
DCC v2 Chaos Engine — Core Utilities
Shared functions for all rollers. Not run directly.
"""

import json
import random
import os
from pathlib import Path

ENGINE_DIR = Path(__file__).parent


def load_floor_tables(floor_number: int) -> dict:
    """Load the JSON table file for a given floor."""
    path = ENGINE_DIR / f"floor_{floor_number:02d}_tables.json"
    if not path.exists():
        raise FileNotFoundError(
            f"No table file found for Floor {floor_number}.\n"
            f"Expected: {path}\n"
            f"Copy floor_XX_tables.json.example and populate it."
        )
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def weighted_pick(entries: list[dict]) -> dict:
    """Pick one entry from a list using 'weight' fields."""
    if not entries:
        raise ValueError("Cannot pick from an empty table.")
    weights = [e["weight"] for e in entries]
    return random.choices(entries, weights=weights, k=1)[0]


def roll_d(sides: int) -> int:
    """Roll a single die with the given number of sides."""
    return random.randint(1, sides)


def format_player_roll(roll_value: int, table_size: int, roller_name: str) -> str:
    """What Doug sees: the roll number and which roller produced it."""
    return f"[{roller_name}] Roll: {roll_value} (of {table_size})"


def format_narrator_result(entry: dict, roller_name: str) -> str:
    """What the narrator sees: the full result text and tags."""
    tags = ", ".join(entry.get("tags", []))
    return (
        f"[{roller_name}] NARRATOR ONLY\n"
        f"  Result: {entry['result']}\n"
        f"  Tags: {tags}"
    )


def divider(label: str = "") -> str:
    if label:
        return f"\n{'='*50}\n  {label}\n{'='*50}"
    return f"\n{'='*50}"
