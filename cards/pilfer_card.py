from cards.card import Card
from random import choice
from cards.hard_hat_card import Hard_Hat
from players.player import Player

class Pilfer(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Pilfer", "Take a random treasure from target opponent's hoard and add it to your hand.")

    def apply_effect(self, game_state):
        Pilfer.played_count += 1
        opponent = game_state.players[int(game_state.current_player().make_decision("choose_opponent", game_state))-1]
        if not opponent.hoard:
            print("Your opponent's hoard is empty")
            return 
        
        unprotected_treasures = [treasure for treasure in opponent.hoard if not self.check_hard_hat(treasure)]

        if not unprotected_treasures:
            print("All treasures in opponent's hoard are protected by Hard Hat.")
            return
            
        random_treasure = choice(unprotected_treasures)
        opponent.hoard.remove(random_treasure)
        game_state.current_player().add_card_to_hand(random_treasure)

        print(f"{game_state.current_player().name} stole {random_treasure.name} from {opponent.name}")
