from card import Card

class Shovel(Card):
    def __init__(self):
        super().__init__("Shovel", "Draw 2 cards")

    def apply_effect(self, game_state):
        for _ in range(2):
            card = game_state.deck.draw_card()
            game_state.current_player().add_card_to_hand(card)