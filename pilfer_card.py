from card import Card
from random import choice
from hard_hat_card import Hard_Hat

class Pilfer(Card):
    def __init__(self):
        super().__init__("Pilfer", "Take a random treasure from target opponent's hoard and add it to your own")

    def apply_effect(self, game_state):
        opponent = super().choose_opponent(game_state)
        if opponent.hoard:
            random_treasure = choice(opponent.hoard)
        else:
            return print("Your opponent's hoard is empty")
        while super().check_hard_hat(random_treasure) == True:
            random_treasure = choice(opponent.hoard)
        opponent.hoard.pop(opponent.hoard.index(random_treasure))
        game_state.current_player().hoard.append(random_treasure)
        print(f"{game_state.current_player().name} Stole {random_treasure} from their opponent!")
        print(f"Debug Message: current player hoards: {game_state.current_player().hoard}")
