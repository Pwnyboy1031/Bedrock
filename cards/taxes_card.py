from cards.card import Card

class Taxes(Card):
    def __init__(self):
        super().__init__("Taxes", "Each player chooses and discards a Treasure from their hoard")
    
    def apply_effect(self, game_state):
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
            user_selection = input().strip()

            while not user_selection or not user_selection.isdigit():
                print("You must choose a treasure to discard.")
                user_selection = input().strip()

            selected_index = int(user_selection) - 1
            selected_index_list = [selected_index]

            if validate_hoard(player, selected_index_list):
                card = player.hoard[selected_index]
                while self.check_hard_hat(card):
                    print(f"{game_state.current_player().hoard[card]} is being protected by Hard Hat. Choose another card.")
                    player.display_hoard()
                    user_selection = input().strip()
                game_state.discard_pile.append(card)
                player.hoard.pop(selected_index)
                