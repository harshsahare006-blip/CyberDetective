# ==========================================
# CyberDetectiveX - Player System
# ==========================================

from core.rank import get_rank


class Player:
    def __init__(self, name):
        self.name = name

        # Progress
        self.xp = 0
        self.rank = get_rank(self.xp)

        # Statistics
        self.cases_solved = 0
        self.minigames_won = 0

        # Collections
        self.achievements = []
        self.inventory = []

    def add_xp(self, amount):
        self.xp += amount
        self.rank = get_rank(self.xp)

    def solve_case(self, xp_reward=200):
        self.cases_solved += 1
        self.add_xp(xp_reward)

    def add_achievement(self, achievement_name):
        if achievement_name not in self.achievements:
            self.achievements.append(achievement_name)

    def add_evidence(self, evidence):
        self.inventory.append(evidence)

    def to_dict(self):
        return {
            "name": self.name,
            "xp": self.xp,
            "rank": self.rank,
            "cases_solved": self.cases_solved,
            "minigames_won": self.minigames_won,
            "achievements": self.achievements,
            "inventory": self.inventory
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])

        player.xp = data.get("xp", 0)
        player.rank = data.get("rank", get_rank(player.xp))

        player.cases_solved = data.get("cases_solved", 0)
        player.minigames_won = data.get("minigames_won", 0)

        player.achievements = data.get("achievements", [])
        player.inventory = data.get("inventory", [])

        return player