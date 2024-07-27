from card import Card
import player


class Back_To_Basics(Card):
    def __init__(self):
        super().__init__("Back To Basics", "Add a card form the discard pile to your hand")

    def apply_effect(self, game_state):
        game_state.display_discard_pile()
        print("Choose a card to add to your hand")
        user_selection = input().strip()
        while game_state.discard_pile[user_selection - 1] not in game_state.discard_pile:
            print("Invalid selection. Please choose a card from the discard pile.")
            game_state.display_discard_pile
            user_selection = input().strip()
        game_state.current_player.add_card_to_hand(game_state.discard_pile[user_selection])
        game_state.discard_pile.pop(user_selection)