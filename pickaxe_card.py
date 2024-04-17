from card import Card

class Pickaxe(Card):
    def __init__(self):
        super().__init__("Pickaxe", "Draw 3 cards")

    def apply_effect(self, game_state):
        for _ in range(3):
            card = game_state.deck.draw_card()
            game_state.current_player().add_card_to_hand(card)