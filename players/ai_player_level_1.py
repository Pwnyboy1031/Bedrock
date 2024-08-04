from players.ai_player import AIPlayer
from cards.treasure_cards import Treasure
from random import choice, sample, randint

class AI_PLayer_Level_1(AIPlayer):
    def __init__(self, name):
        super().__init__(name)

    def make_decision(self, decision_function_name, *args):
        method = getattr(self, decision_function_name, None)
        if decision_function_name == "choose_treasure_to_discard":
            return self.choose_lowest_treasure(*args)
        if method:
            return method(*args)
        else:
            print(f"Error: Method {decision_function_name} not found")
            return None
        
    def evaluate_gamestate():
        pass

    def choose_treasure_in_hand(self):
        #choose treasure to play during treasure phase
        treasure_cards = [card for card in self.hand if isinstance(card, Treasure)]
        
        if not treasure_cards:
            print(f"{self.name} has no treasure cards to play. Moving to Main phase.")
            return []
        
        # currently, playing 2 treasures is usually always optimal
        num_treasures_to_play = 2

        # Ensure we don't play more than 1 treasure if we only have 1
        num_treasures_to_play = min(num_treasures_to_play, len(treasure_cards))

        selected_treasures = []

        for _ in range(num_treasures_to_play):
            treasure_index = int(self.choose_highest_treasure(treasure_cards)) - 1
            if treasure_index is not None:
                selected_treasures.append(treasure_cards[treasure_index])
                treasure_cards.pop(treasure_index) 

        #convert to what human player would choose
        selected_indices = [self.hand.index(treasure) + 1 for treasure in selected_treasures]

        indices_string = ",".join(map(str, selected_indices))

        return indices_string
    
    def is_winning(self, game_state):
        winning_score = 0
        self_score = game_state.scoreboard.get(self.name, 0
                                               )
        for player, score in game_state.scoreboard.items():
            if score > winning_score:
                winning_score = score
        return self_score == winning_score
    
    def choose_lowest_treasure(self, set):
        lowest = 5
        lowest_index = -1
        for card in set:
            if card.points < lowest:
                lowest_index = set.index(card)
        return str(lowest_index + 1)
    
    def choose_highest_treasure(self, set):
        highest = -1
        highest_index = -1
        for card in set:
            if card.points > highest:
                highest_index = set.index(card)
        return str(highest_index + 1) 