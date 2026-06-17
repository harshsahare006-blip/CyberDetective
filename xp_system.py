# ==========================================
# CyberDetectiveX - XP System
# ==========================================

CASE_SOLVED_XP = 200
MINIGAME_WIN_XP = 30
PERFECT_CASE_XP = 100
EVIDENCE_FOUND_XP = 50
DAILY_MISSION_XP = 20


def reward_case(player):
    player.add_xp(CASE_SOLVED_XP)


def reward_perfect_case(player):
    player.add_xp(PERFECT_CASE_XP)


def reward_evidence(player):
    player.add_xp(EVIDENCE_FOUND_XP)


def reward_minigame(player):
    player.add_xp(MINIGAME_WIN_XP)


def reward_daily(player):
    player.add_xp(DAILY_MISSION_XP)