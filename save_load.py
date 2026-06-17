# ==========================================
# CyberDetectiveX - Save & Load System
# ==========================================

import json
import os

from core.player import Player

SAVE_FILE = "data/saves.json"


def save_game(player):
    """
    Save player progress to JSON file
    """

    os.makedirs("data", exist_ok=True)

    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(
            player.to_dict(),
            file,
            indent=4
        )


def load_game():
    """
    Load saved player data
    """

    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return Player.from_dict(data)

    except Exception:
        return None