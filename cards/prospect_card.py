from cards.scry_Card import ScryCard

class Prospect(ScryCard):
    played_count = 0

    def __init__(self):
        super().__init__("Prospect", 4)

    def apply_effect(self, game_state):
        Prospect.played_count += 1
        return super().apply_effect(game_state)