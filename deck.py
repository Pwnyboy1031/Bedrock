from card import Card
from cards import initialize_cards
import random

class Deck:
    def __init__(self):
        self.cards = initialize_cards()
        
    def add_card_to_top(self, card):
        self.cards.insert(0, card)

    def add_card_to_bottom(self, card):
        self.cards.append(card)
    
    def shuffle(self):
       return random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0)
    
    def reveal_top_cards(self, num_cards):
        revealed_cards = self.cards[:num_cards]
        return revealed_cards