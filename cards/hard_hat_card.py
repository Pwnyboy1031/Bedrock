from cards.card import Card
from players.player import player

class Hard_Hat(Card):
    def __init__(self):
        super().__init__("Hard Hat", "Attach this card to a Treasure in your hoard. That treasure cannot be moved from your hoard")

    def apply_effect(self, game_state):
        game_state.current_player().display_hoard()
        print("Select which treasure to attach Hard Hat to.")
        selected_treasure = int(player.make_decision("choose_from_set(player.hoard)"))
        selected_treasure_index = game_state.current_player().hoard.index(selected_treasure)
        game_state.current_player().hoard[selected_treasure_index - 1 ].attachments.append(self)
