from cards.scry_Card import ScryCard

class Prospect(ScryCard):
    def __init__(self):
        super().__init__("Prospect", 4)

    def apply_effect(self, game_state):
        return super().apply_effect(game_state)