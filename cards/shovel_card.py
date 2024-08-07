from cards.card import Card

class Shovel(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Shovel", "Draw 2 cards.")

    def apply_effect(self, game_state):
        Shovel.played_count += 1
        from game.game_logic import draw_card
        for _ in range(2):
            draw_card(game_state)