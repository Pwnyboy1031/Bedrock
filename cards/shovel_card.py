from card import Card

class Shovel(Card):
    def __init__(self):
        super().__init__("Shovel", "Draw 2 cards")

    def apply_effect(self, game_state):
        from game.game_logic import draw_card
        for _ in range(2):
            draw_card(game_state)