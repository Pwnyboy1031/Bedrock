from players.player import Player
from game.game_state import GameState
from cards.treasure_cards import Treasure
from random import random, choice, sample

class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_decision(self, decision_function_name):
       method = getattr(self, decision_function_name, None)
       if method:
           return method()
       else:
           print(f"Error: Method {decision_function_name} not found")
           return None

    def choose_treasure_in_hand(self):
        #choose treasure to play during treasure phase
        treasure_cards = [card for card in self.hand if isinstance(card, Treasure)]
        
        if not treasure_cards:
            print(f"{self.name} has no treasure cards to play. Moving to Main phase.")
            return []
        # randomly decide to play one or 2 treasures
        num_treasures_to_play = choice([1,2])

        # Ensure we don't play more than 1 treasure if we only have 1
        num_treasures_to_play = min(num_treasures_to_play, len(treasure_cards))

        selected_treasures = sample(treasure_cards, num_treasures_to_play)

        #convert to what human player would choose
        selected_indices = [self.hand.index(treasure) + 1 for treasure in selected_treasures]

        indices_string = ",".join(map(str, selected_indices))

        return indices_string


    def choose_action_card_in_hand(self):
        #choose spells to play during main phase
        action_cards = [card for card in self.hand if not isinstance(card, Treasure)]

        if not action_cards:
            print(f"{self.name} has no action cards to play. Ending turn.")
            return []
        # randomly decide to play one or 2 action cards
        num_actions_to_play = choice([1,2])

        #ensure we don't play more than 1 action if we only have 1 in hand
        num_actions_to_play = min(num_actions_to_play, len(action_cards))

        selected_actions = sample(action_cards, num_actions_to_play)

        #convert to what human player would input
        selected_indices = [self.hand.index(action) + 1 for action in selected_actions]

        indices_string = ",".join(map(str, selected_indices))

        return indices_string

    
    def scry(game_state):
        pass

    def choose_from_set(set):
        choice = choice(set)
        return choice

    def choose_opponent(game_state):
        pass

    def choose_hard_hat_target(game_state):
        pass
