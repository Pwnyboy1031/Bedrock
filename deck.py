from card import Card
from shovel_card import Shovel
from pickaxe_card import Pickaxe
import random

class Deck:
    def __init__(self):
        shovel_cards = [Shovel() for _ in range(10)] #change back to 10
        pickaxe_cards = [Pickaxe() for _ in range(5)]
        self.cards = shovel_cards + pickaxe_cards
        

    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
       return random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0)