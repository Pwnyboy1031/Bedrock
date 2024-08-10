from players.ai_player import AIPlayer
from cards.treasure_cards import Treasure
from random import choice, sample, randint

class AI_Player_Level_1(AIPlayer):
    def __init__(self, name):
        super().__init__(name)

    def make_decision(self, decision_function_name, *args):
        method = getattr(self, decision_function_name, None)
        if decision_function_name == "choose_action_card_in_hand":
            return self.choose_action_card_in_hand(*args)
        if decision_function_name == "choose_treasure_to_discard":
            return self.choose_lowest_treasure(*args)
        if decision_function_name == "choose_opponent":
            return self.choose_winning_opponent(*args)
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
    
    def choose_action_card_in_hand(self, game_state):
        # choose spells to play during main phase
        action_cards = [card for card in self.hand if not isinstance(card, Treasure)]

        if not action_cards:
            print(f"{self.name} has no action cards to play. Ending turn.")
            return []
        
        # Strategy - draw when winning to get bedrock
        draw_cards = [card for card in action_cards if card.name in ["Shovel", "Pickaxe", "Earthquake", "Trade Secrets", "Investment"]]
        prolong_cards = [card for card in action_cards if card.name in ["Deep Exploration", "Tunnel Collapse", "Pilfer"]]
        other_cards = [card for card in action_cards if card.name not in draw_cards and card.name not in prolong_cards]

        selected_actions = []
        if self.is_winning(game_state):
            print("Trying Draw Strategy")
            num_draw_cards_to_play = min(len(draw_cards), 2)
            selected_draw_cards = sample(draw_cards, num_draw_cards_to_play) if draw_cards else []
            selected_actions.extend(selected_draw_cards)

            if len(selected_actions) < 2:
                num_other_cards_to_play = min(len(other_cards), 2 - len(selected_actions))
                selected_other_cards = sample(other_cards, num_other_cards_to_play) if other_cards else []
                selected_actions.extend(selected_other_cards)

        else:
            print("Avoiding drawing")
            num_prolong_cards_to_play = min(len(prolong_cards), 2)
            selected_prolong_cards = sample(prolong_cards, num_prolong_cards_to_play) if prolong_cards else []
            selected_actions.extend(selected_prolong_cards)

            if len(selected_actions) < 2:
                num_other_cards_to_play = min(len(other_cards), 2 - len(selected_actions))
                selected_other_cards = sample(other_cards, num_other_cards_to_play) if other_cards else []
                selected_actions.extend(selected_other_cards)

            if len(selected_actions) < 2:
                num_draw_cards_to_play = min(len(draw_cards), 2 - len(selected_actions))
                selected_draw_cards = sample(draw_cards, num_draw_cards_to_play) if draw_cards else []
                selected_actions.extend(selected_draw_cards)

        # Convert to what human player would input
        selected_indices = [self.hand.index(action) + 1 for action in selected_actions]

        indices_string = ",".join(map(str, selected_indices))

        return indices_string
    
    def is_winning(self, game_state):
        winning_score = 0
        self_score = game_state.scoreboard.get(self.name, 0)
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
                lowest = card.points
        return str(lowest_index + 1)
    
    def choose_highest_treasure(self, set):
        highest = -1
        highest_index = -1
        for card in set:
            if card.points > highest:
                highest_index = set.index(card)
        return str(highest_index + 1) 
    
    def choose_winning_opponent(self, game_state):
        winning_player_index = -1
        opponents = []
        for index, player in enumerate(game_state.players):
            if index != game_state.current_player_index:
                opponents.append(player)
        for player in opponents:
            if player.is_winning(game_state):
                winning_player_index = game_state.players.index(player)

        return str(winning_player_index + 1)