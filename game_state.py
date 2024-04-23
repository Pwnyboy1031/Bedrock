class GameState:
    def __init__(self, players, deck):
        self.players = players
        self.current_player_index = 0
        self.deck = deck
        self.scoreboard = {player.name: 0 for player in players}

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def current_player(self):
        return self.players[self.current_player_index]
    
    def update_scoreboard(self, player_name, points):
        if player_name in self.scoreboard:
            self.scoreboard[player_name] += points
        else:
            print(f"Player {player_name} not found in scoreboard.")
    
    def get_scores(self):
        return self.scoreboard
    