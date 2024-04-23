from scry_Card import ScryCard

class Spelunk(ScryCard):
    def __init__(self):
        super().__init__("Spelunk", 2)

    def apply_effect(self, game_state):
        return super().apply_effect(game_state)