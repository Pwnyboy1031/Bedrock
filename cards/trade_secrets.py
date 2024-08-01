from cards.card import Card
from random import choice

class Trade_Secrets(Card):
    def __init__(self):
        super().__init__("Trade Secrets", "Take 2 random cards from an opponent's hand and add them to your own.")

    def apply_effect(self, game_state):
        game_state.display_opponents()
        print("Choose an opponent to take up to 2 cards from")
        user_selection = input().strip()
        while game_state.players[int(user_selection) - 1] not in game_state.players:
            print("Please select a valid player")
            user_selection = input().strip()
        selectedOpponent = game_state.players[int(user_selection)-1]
        for rand_card_index in range(2):
            if selectedOpponent.hand:
                rand_card_index = selectedOpponent.hand.index(choice(selectedOpponent.hand))
                card = selectedOpponent.hand[rand_card_index]
                selectedOpponent.hand.pop(rand_card_index)
                game_state.current_player().hand.append(card)
                print(f"{(game_state.current_player().name)} stole {card.name} from {selectedOpponent.name}!")

