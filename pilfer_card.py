from card import Card
from random import choice

class Pilfer(Card):
    def __init__(self):
        super().__init__("Pilfer", "Take a random treasure from target opponent's hoard and add it to your own")

    def apply_effect(self, game_state):
        opponent = super().choose_opponent(game_state)
        random_treasure = choice(opponent.hoard)
        opponent.hoard.pop(opponent.hoard.index(random_treasure))
        game_state.current_player().hoard.append(random_treasure)
        print(f"Debug Message: current player hoards: {game_state.current_player().hoard}")
