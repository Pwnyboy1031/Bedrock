from card import Card

class Investment(Card):
    def __init__(self):
        super().__init__("Investment", "Remove X treasures from your hoard. Draw double X cards")

    def apply_effect(self, game_state):
        print()
        game_state.current_player().display_hoard()