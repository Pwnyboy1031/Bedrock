from card import Card


class Investment(Card):
    def __init__(self):
        super().__init__("Investment", "Remove X treasures from your hoard. Draw double X cards.")

    def apply_effect(self, game_state):
        from game_logic import add_to_discard_pile, validate_hoard, remove_from_hoard, draw_card
        game_state.current_player().display_hoard()
        print("Enter selection for 1 card or 'selection, selection,....' for multiple cards.")
        user_selection = input().strip()
        if not user_selection:
            return [] # return empty list if no input
        card_indices = [int(index) - 1 for index in user_selection.split(',')]     
        if validate_hoard(game_state.current_player(), card_indices):
            self.apply_effect(game_state)
        for card in card_indices:
            if super().check_hard_hat(game_state.current_player.hoard[card]) == True:
                self.apply_effect(game_state)
        for index in card_indices: # add selections to discard and draw
            card = game_state.current_player().hoard[index]
            add_to_discard_pile(game_state, card)
            print(f"{game_state.current_player().name} discarded {card.name} from their hoard!")
            draw_card(game_state)
            draw_card(game_state)
            
        for index in sorted(card_indices, reverse=True): #clean up the hoard, reverse hoard so that the indexes leave no spaces
            remove_from_hoard(game_state, game_state.current_player(), index)