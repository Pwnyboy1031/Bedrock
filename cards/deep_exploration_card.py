from cards.card import Card

class Deep_Exploration(Card):
    played_count = 0

    def __init__(self):
        super().__init__("Deep Exploration", "The next time the Bedrock card is drawn, ignore its effect and shuffle it back into the Mine. When Deep Exploration resolves, remove it from the game.")

    def apply_effect(self, game_state):
        Deep_Exploration.played_count += 1
        game_state.deep_exploration_active = True