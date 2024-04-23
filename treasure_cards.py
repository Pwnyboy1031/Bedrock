from card import Card


class Treasure(Card):
    def __init__(self, name, points):
        super().__init__(name, f"This Treasure is worth {points} point(s) at the end of the game if it is in your hoard")
        self.points = points
        self.name = name

    def apply_effect(self, game_state):
        from game_logic import add_to_hoard
        add_to_hoard(game_state.current_player(), self)
        game_state.update_scoreboard(game_state.current_player().name, self.points)
    
class Ruby(Treasure):
    def __init__(self):
        super().__init__("Ruby", 1)

class Sapphire(Treasure):
    def __init__(self):
        super().__init__("Sapphire", 2)

class Emerald(Treasure):
    def __init__(self):
        super().__init__("Emerald", 3)

class Diamond(Treasure):
    def __init__(self):
        super().__init__("Diamond", 4)
