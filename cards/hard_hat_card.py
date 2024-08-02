from cards.card import Card

class Hard_Hat(Card):
    def __init__(self):
        super().__init__("Hard Hat", "Attach this card to a Treasure in your hoard. That treasure cannot be moved from your hoard")

    def apply_effect(self, game_state):
        player = game_state.current_player()
        player.display_hoard()
        print("Select which treasure to attach Hard Hat to.")
        selected_treasure = int(player.make_decision("choose_from_set", player.hoard))
        selected_treasure_index = game_state.current_player().hoard.index(selected_treasure)
        game_state.current_player().hoard[selected_treasure_index - 1 ].attachments.append(self)
