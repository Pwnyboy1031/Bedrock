from cards.card import Card
import players.player as player


class Back_To_Basics(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Back To Basics", "Add a card from the discard pile to your hand.")

    def apply_effect(self, game_state):
        Back_To_Basics.played_count += 1
        game_state.display_discard_pile()
        print("Choose a card to add to your hand")
        user_selection = int((game_state.current_player().make_decision("choose_from_set", game_state.discard_pile)))
        while game_state.discard_pile[user_selection - 1] not in game_state.discard_pile:
            print("Invalid selection. Please choose a card from the discard pile.")
            game_state.display_discard_pile
            user_selection = game_state.current_player().make_decision("choose_from_set(game_state.discard_pile)")
        game_state.current_player().add_card_to_hand(game_state.discard_pile[user_selection - 1])
        game_state.discard_pile.pop(user_selection -1)