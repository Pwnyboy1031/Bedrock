from card import Card
from deck import Deck
from game_state import GameState
from game_logic import draw_card, play_cards, resolve_effects, take_turn
from shovel_card import Shovel
from pickaxe_card import Pickaxe
from player import Player
import game_logic
from spelunk_card import Spelunk
from survey_card import Survey
from treasure_cards import Ruby
import random

        
def main():
    game_state = game_logic.initialize_game()
    take_turn(game_state)
    
  



if __name__ == "__main__":
    main()