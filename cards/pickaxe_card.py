from cards.card import Card

class Pickaxe(Card):
    def __init__(self):
        super().__init__("Pickaxe", "Draw 3 cards")

    def apply_effect(self, game_state):
        from game.game_logic import draw_card
        for _ in range(3):
            draw_card(game_state)