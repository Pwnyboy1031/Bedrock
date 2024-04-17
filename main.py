from card import Card
from deck import Deck
from game_state import GameState
from game_logic import draw_card, play_cards, resolve_effects
from shovel_card import Shovel
from pickaxe_card import Pickaxe
from player import Player
import game_logic
import random

# shovel_card = Shovel() 
# pickaxe_card = Pickaxe()

# shovel_cards = [Shovel() for _ in range(10)]
# pickaxe_cards = [Pickaxe() for _ in range(5)]

#initialize players
player1 = Player("Taylor")
player2 = Player("Ryan")

#initialize Deck
deck = Deck()

#shuffle deck
random.shuffle(deck.cards)



## Define players
players = [player1, player2]


# intialize cards
game_state = GameState(players, deck)



        
def main():
    game_logic.initialize_game()
    print(game_state.players, game_state.deck.cards)
    player1.display_hand()
    player2.display_hand()



  



if __name__ == "__main__":
    main()