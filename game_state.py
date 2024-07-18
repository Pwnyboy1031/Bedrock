class GameState:
    def __init__(self, players, deck):
        self.players = players
        self.current_player_index = 0
        self.deck = deck
        self.discard_pile = []
        self.scoreboard = {player.name: 0 for player in players}
        self.phases = ["Treasure", "Main"]
        self.phase = self.phases[0]
        self.bedrock_count = 0
        self.bedrock_limit = len(players) + 1
        self.game_over = False

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        
    
    def current_player(self):
        return self.players[self.current_player_index]
    
    def update_scoreboard(self, player):
        self.scoreboard[player.name] = 0
        for treasure in player.hoard:
            self.scoreboard[player.name] += treasure.points
        print(f"The scoreboard has been updated\n{self.scoreboard}")
    
    def get_scores(self):
        return self.scoreboard
    