# ==========================================
# CyberDetectiveX - Achievement System
# ==========================================

ACHIEVEMENTS = {
    "FIRST_CASE": "First Case Closed",
    "ROOKIE": "Rookie Investigator",
    "THREAT_HUNTER": "Threat Hunter",
    "FORENSICS_MASTER": "Forensics Master",
    "LEGEND": "Legendary Detective"
}


def check_achievements(player):

    unlocked = []

    if player.cases_solved >= 1:
        unlocked.append(ACHIEVEMENTS["FIRST_CASE"])

    if player.xp >= 500:
        unlocked.append(ACHIEVEMENTS["ROOKIE"])

    if player.xp >= 1500:
        unlocked.append(ACHIEVEMENTS["THREAT_HUNTER"])

    if player.xp >= 3000:
        unlocked.append(ACHIEVEMENTS["FORENSICS_MASTER"])

    if player.xp >= 5000:
        unlocked.append(ACHIEVEMENTS["LEGEND"])

    for achievement in unlocked:
        if achievement not in player.achievements:
            player.add_achievement(achievement)