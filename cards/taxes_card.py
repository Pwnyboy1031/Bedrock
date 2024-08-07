from cards.card import Card

class Taxes(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Taxes", "Each player chooses and discards a Treasure from their hoard.")
    
    def apply_effect(self, game_state):
        Taxes.played_count += 1
        from game.game_logic import validate_hoard
        for player in game_state.players:
            if not player.hoard:
                print(f"{player.name}'s hoard has no valid targets")
                continue
            
            unprotected_treasures = [treasure for treasure in player.hoard if not self.check_hard_hat(treasure)]

            if not unprotected_treasures:
                print(f"All of {player.name}'s treasures are protected by Hard Hat ")
                continue

            print(f"{player.name}, choose a treasure to discard from your hoard")
            player.display_hoard()
            user_selection = player.make_decision("choose_treasure_to_discard", player.hoard)

            while not user_selection or not user_selection.isdigit():
                print("You must choose a treasure to discard.")
                user_selection = player.make_decision("choose_treasure_to_discard", player.hoard)

            selected_index = int(user_selection) - 1
            selected_index_list = [selected_index]

            if validate_hoard(player, selected_index_list):
                card = player.hoard[selected_index]
                while self.check_hard_hat(card):
                    print(f"{card.name} is being protected by Hard Hat. Choose another card.")
                    player.display_hoard()
                    selected_index = int(player.make_decision("choose_from_set", player.hoard))
                    card = player.hoard[selected_index - 1]
                game_state.discard_pile.append(card)
                player.hoard.pop(selected_index - 1)
                