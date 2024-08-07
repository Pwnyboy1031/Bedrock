from cards.card import Card

class Hard_Hat(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Hard Hat", "Attach this card to a Treasure in your hoard. That treasure cannot be moved from your hoard.")

    def apply_effect(self, game_state):
        Hard_Hat.played_count += 1
        player = game_state.current_player()
        player.display_hoard()
        print("Select which treasure to attach Hard Hat to.")
        selected_treasure_index = int(player.make_decision("choose_from_set", player.hoard)) - 1
        targeted_treasure = player.hoard[selected_treasure_index]
        targeted_treasure.attachments.append(self)

