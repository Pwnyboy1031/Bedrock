from cards.card import Card
from game.game_state import GameState


class ScryCard(Card):
    def __init__(self, name, scry_number):
        super().__init__(name, f"Scry {scry_number}")
        self.scry_number = scry_number


    def apply_effect(self, game_state):
        from game.game_logic import reveal_cards
        scry_number = self.scry_number
        scryed_cards = game_state.deck.reveal_top_cards(scry_number)
        options = list(scryed_cards)
        for index, card in enumerate (scryed_cards):
            print("Select a card")
            reveal_cards(options)
            choice = int(game_state.current_player().make_decision("choose_from_set", options)) - 1
            selected_card = options[choice]
            print(f"Would you like to place {selected_card.name} on:\n 1. Top of the deck\n 2. Bottom of the deck")
            placement_selection = game_state.current_player().make_decision("choose_from_set", [1,2])
            # Check for valid placement selection
            while placement_selection not in ['1', '2']:
                print("Invalid selection Please select 1 or 2")
                placement_selection = game_state.current_player().make_decision("choose_from_set",[1,2])
            if placement_selection == '1':
                print(f"Placed {selected_card.name} on top of deck")
                game_state.deck.cards.remove(selected_card)
                game_state.deck.add_card_to_top(selected_card)
                options.remove(selected_card)
            else:
                print(f"Placed {selected_card.name} on bottom of deck")
                game_state.deck.add_card_to_bottom(selected_card)
                game_state.deck.cards.remove(selected_card)
                options.remove(selected_card)

