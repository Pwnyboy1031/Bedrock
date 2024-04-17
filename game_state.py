class GameState:
    def __init__(self, players, deck):
        self.players = players
        self.current_player_index = 0
        self.deck = deck

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def current_player(self):
        return self.players[self.current_player_index]