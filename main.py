from card import Card
from deck import Deck
from game_state import GameState
from game_logic import draw_card, play_cards, resolve_effects, take_turn
from shovel_card import Shovel
from pickaxe_card import Pickaxe
from player import Player
import game_logic
import random

# shovel_card = Shovel() 
# pickaxe_card = Pickaxe()

# shovel_cards = [Shovel() for _ in range(10)]
# pickaxe_cards = [Pickaxe() for _ in range(5)]
1



        
def main():
    game_state = game_logic.initialize_game()
    #print(game_state.players, game_state.deck.cards)
    game_state.players[0].display_hand()
    game_state.players[1].display_hand()
    take_turn(game_state)


  



if __name__ == "__main__":
    main()