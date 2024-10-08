class Card:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect
        self.played_count = 0
        

    def apply_effect(self, game_state):
        pass #placeholder for card effects

    @staticmethod
    def choose_opponent(game_state):
        game_state.display_opponents()
        print("Choose an opponent")
        user_selection = game_state.current_player().make_decision("choose_opponent", game_state)
        while game_state.players[int(user_selection) - 1] not in game_state.players:
            print("Please select a valid player")
            user_selection = game_state.current_player().make_decision("choose_opponent", game_state)
        selectedOpponent = game_state.players[int(user_selection)-1]
        return(selectedOpponent)
    @staticmethod
    def check_hard_hat(target):
        from cards.hard_hat_card import Hard_Hat 
        if target.attachments:
            for attachment in target.attachments:
                if isinstance(attachment, Hard_Hat):
                    return True
        return False