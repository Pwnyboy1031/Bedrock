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
        self.bedrock_limit = len(players)
        self.game_over = False
        self.deep_exploration_active = False
        self.turns = 0
        self.rounds = 0

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players) 
        
    
    def current_player(self):
        return self.players[self.current_player_index]
    
    def update_scoreboard(self):
        for player in self.players:
            self.scoreboard[player.name] = 0
            for treasure in player.hoard:
                self.scoreboard[player.name] += treasure.points
        print(f"The scoreboard has been updated\n{self.scoreboard}")
        print()
    
    def get_scores(self):
        return self.scoreboard
    
    def display_discard_pile(self):
        print("Discard Pile:")
        for index, card in enumerate(self.discard_pile):
            print(f"{index + 1}.  {card.name}")
        print()

    def display_opponents(self):
        print("Opponents:")
        for index, player, in enumerate(self.players):
            if index != self.current_player_index:
                print(f"{index + 1}.  {player.name}")
        print()    