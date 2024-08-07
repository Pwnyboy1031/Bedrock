import json
from collections import defaultdict
import game.game_logic
from game.game_logic import take_turn




def run_game(game_state):
    while True:
        while not game_state.game_over:
            take_turn(game_state)
        result = game.game_logic.game_over(game_state)
        if result is not None:
            return result

def run_simulation(num_games):
    results = {
        'games_played': 0,
        'wins':defaultdict(int),
        'scores':defaultdict(list)
    }

    for _ in range(num_games):
        game_state = game.game_logic.initialize_game()
        
        winner, winner_score = run_game(game_state)

        results['games_played'] += 1
        results['wins'][winner] += 1

        for player, score in game_state.get_scores().items():
            results['scores'][player].append(score)
            
    return results