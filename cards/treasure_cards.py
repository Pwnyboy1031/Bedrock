from cards.card import Card


class Treasure(Card):
    played_count = 0
    def __init__(self, name, points):
        super().__init__(name, f"This Treasure is worth {points} point(s) at the end of the game if it is in your hoard.")
        self.points = points
        self.name = name
        self.attachments = []

    def apply_effect(self, game_state):
        from game.game_logic import add_to_hoard
        add_to_hoard(game_state, game_state.current_player(), self)
    
class Ruby(Treasure):
    played_count = 0
    def __init__(self):
        super().__init__("Ruby", 1)
    def apply_effect(self, game_state):
        Ruby.played_count += 1
        return super().apply_effect(game_state)

class Sapphire(Treasure):
    played_count = 0
    def __init__(self):
        super().__init__("Sapphire", 2)
    def apply_effect(self, game_state):
        Sapphire.played_count += 1
        return super().apply_effect(game_state)

class Emerald(Treasure):
    played_count = 0
    def __init__(self):
        super().__init__("Emerald", 3)
    def apply_effect(self, game_state):
        Emerald.played_count += 1
        return super().apply_effect(game_state)

class Diamond(Treasure):
    played_count = 0
    def __init__(self):
        super().__init__("Diamond", 4)
    def apply_effect(self, game_state):
        Diamond.played_count += 1
        return super().apply_effect(game_state)
