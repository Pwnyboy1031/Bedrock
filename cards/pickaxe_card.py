from cards.card import Card

class Pickaxe(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Pickaxe", "Draw 3 cards.")

    def apply_effect(self, game_state):
        Pickaxe.played_count += 1
        from game.game_logic import draw_card
        for _ in range(3):
            draw_card(game_state)