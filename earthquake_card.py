from card import Card



class Earthquake(Card):
    def __init__(self):
        super().__init__("Earthquake", "Shuffle all player's hands into the Mine. Then each player draws 5 cards.")
    
    def apply_effect(self, game_state):
        for player in game_state.players:
            for card in player.hand[:]:
                game_state.deck.add_card_to_top(card)
            player.hand.clear()
        game_state.deck.shuffle()
        for _ in range(5):
            for player in game_state.players:
                from game_logic import draw_card
                draw_card(game_state)
                game_state.next_turn()