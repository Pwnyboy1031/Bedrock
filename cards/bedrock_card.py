from cards.card import Card
from game.game_state import GameState

class Bedrock(Card):
    played_count = 0
    def __init__(self):
        super().__init__("Bedrock", f"If bedrock has been drawn X + the number of players time(s), the game is over.")

    def apply_effect(self, game_state):
        Bedrock.played_count += 1
        from game.game_logic import draw_card, game_over
        print("BEDROCK!")
        if game_state.deep_exploration_active == True:
            print(f"BEDROCK COUNT IS NOW {game_state.bedrock_count}")
            game_state.deck.add_card_to_top(self)
            game_state.deck.shuffle()
            game_state.deep_exploration_active = False
            return
        game_state.bedrock_count += 1
        print(f"BEDROCK COUNT IS NOW {game_state.bedrock_count}")
        if game_state.bedrock_count >= game_state.bedrock_limit:
            game_state.game_over = True   
        else:
            game_state.deck.add_card_to_top(self)  
            game_state.deck.shuffle()
            draw_card(game_state)
            