from card import Card
from random import choice
from hard_hat_card import Hard_Hat

class Pilfer(Card):
    def __init__(self):
        super().__init__("Pilfer", "Take a random treasure from target opponent's hoard and add it to your own")

    def apply_effect(self, game_state):
        opponent = self.choose_opponent(game_state)
        if not opponent.hoard:
            print("Your opponent's hoard is empty")
            return 
        
        unprotected_treasures = [treasure for treasure in opponent.hoard if not self.check_hard_hat(treasure)]

        if not unprotected_treasures:
            print("All treasures in opponent's hoard are protected by Hard Hat.")
            return
            
        random_treasure = choice(unprotected_treasures)
        opponent.hoard.remove(random_treasure)
        game_state.current_player().hoard.append(random_treasure)

        print(f"{game_state.current_player().name} Stole {random_treasure.name} from {opponent.name}")
        print(f"Debug Message: {game_state.current_player().name}'s hoard: {[t.name for t in game_state.current_player().hoard]}")
