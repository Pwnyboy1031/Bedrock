from cards.scry_Card import ScryCard

class Survey(ScryCard):
    played_count = 0

    def __init__(self):
        super().__init__("Survey", 3)

    def apply_effect(self, game_state):
        Survey.played_count += 1
        return super().apply_effect(game_state)