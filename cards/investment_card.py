from cards.card import Card


class Investment(Card):
    def __init__(self):
        super().__init__("Investment", "Remove X treasures from your hoard. Draw double X cards.")

    def apply_effect(self, game_state):
        from game.game_logic import add_to_discard_pile, validate_hoard, remove_from_hoard, draw_card

        player = game_state.current_player()
        player.display_hoard()
        print("Enter selection for 1 card or 'selection, selection,....' for multiple cards.")
        user_selection = player.make_decision("choose_lowest_treasure", player.hoard)

        if not user_selection:
            return [] # return empty list if no input
        
        card_indices = [int(index) - 1 for index in user_selection.split(',')]

        if validate_hoard(player, card_indices):
            valid_indices = []
            for index in card_indices:
                card = player.hoard[index]
                if self.check_hard_hat(card):
                    print(f"{card.name} is being protected by Hard Hat. Your target fizzles.")
                    return
                else:
                    valid_indices.append(index)

            for index in valid_indices: # add selections to discard and draw
                card = player.hoard[index]
                add_to_discard_pile(game_state, card)
                print(f"{player.name} discarded {card.name} from their hoard!")
                draw_card(game_state)
                draw_card(game_state)
                
            for index in sorted(valid_indices, reverse=True): #clean up the hoard, reverse hoard so that the indexes leave no spaces
                remove_from_hoard(game_state, player, index)