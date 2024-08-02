from cards.card import Card

class Tunnel_Collapse(Card):
    def __init__(self):
        super().__init__("Tunnel Collapse", "Shuffle the discard pile back into the Mine.")
    
    def apply_effect(self, game_state):
        for card in game_state.discard_pile[:]:
            game_state.deck.add_card_to_top(card)

        game_state.discard_pile.clear()
        game_state.deck.shuffle()