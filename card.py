class Card:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
        

    def apply_effect(self, game_state):
        pass #placeholder for card effects

    @staticmethod
    def choose_opponent(game_state):
        game_state.display_opponents()
        print("Choose an opponent")
        user_selection = input().strip()
        while game_state.players[int(user_selection) - 1] not in game_state.players:
            print("Please select a valid player")
            user_selection = input().strip()
        selectedOpponent = game_state.players[int(user_selection)-1]
        return(selectedOpponent)