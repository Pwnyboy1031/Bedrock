from card import Card
from game_state import GameState

class Bedrock(Card):
    def __init__(self):
        super().__init__("Bedrock", f"If bedrock has been drawn X + the number of players time(s), the game is over.")

    def apply_effect(self, game_state):
        from game_logic import draw_card, game_over
        print("BEDROCK!")
        print(f"BEDROCK COUNT IS NOW {game_state.bedrock_count}")
        if game_state.deep_exploration_active == True:
            game_state.deck.add_card_to_top(game_state.deck, self)
            game_state.deck.shuffle()
            game_state.deep_exploration_active = False
            return
        game_state.bedrock_count += 1
        if game_state.bedrock_count >= game_state.bedrock_limit:
            game_over(game_state)# end game    
        else:
            game_state.deck.add_card_to_top(self)  
            game_state.deck.shuffle()
            draw_card(game_state)
            