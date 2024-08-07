from cards.card import Card
from random import choice

class Trade_Secrets(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Trade Secrets", "Take 2 random cards from an opponent's hand and add them to your own.")

    def apply_effect(self, game_state):
        Trade_Secrets.played_count += 1
        print("Choose an opponent to take up to 2 cards from")
        selectedOpponent = self.choose_opponent(game_state)
        for rand_card_index in range(2):
            if selectedOpponent.hand:
                rand_card_index = selectedOpponent.hand.index(choice(selectedOpponent.hand))
                card = selectedOpponent.hand[rand_card_index]
                selectedOpponent.hand.pop(rand_card_index)
                game_state.current_player().hand.append(card)
                print(f"{(game_state.current_player().name)} stole {card.name} from {selectedOpponent.name}!")

