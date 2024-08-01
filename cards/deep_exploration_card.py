from card import Card

class Deep_Exploration(Card):
    def __init__(self):
        super().__init__("Deep Exploration", "The next time the Bedrock card is drawn, ignore its effect and shuffle it back into the Mine. When Deep Exploration resolves, remove it from the game.")

    def apply_effect(self, game_state):
        game_state.deep_exploration_active = True