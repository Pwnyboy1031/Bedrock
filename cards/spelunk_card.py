from cards.scry_Card import ScryCard

class Spelunk(ScryCard):
    played_count = 0

    def __init__(self):
        super().__init__("Spelunk", 2)

    def apply_effect(self, game_state):
        Spelunk.played_count += 1
        return super().apply_effect(game_state)