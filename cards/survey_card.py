from cards.scry_Card import ScryCard

class Survey(ScryCard):
    def __init__(self):
        super().__init__("Survey", 3)

    def apply_effect(self, game_state):
        return super().apply_effect(game_state)