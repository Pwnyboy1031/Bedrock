import json
from collections import defaultdict
import game.game_logic
from game.game_logic import take_turn
from cards.card import Card
from cards.treasure_cards import Treasure




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
        'card_play_counts':defaultdict(int),
        'scores':defaultdict(list),
        'avg_rounds': 0
    }

    total_rounds = 0

    for _ in range(num_games):
        game_state = game.game_logic.initialize_game()
        
        winner, winner_score, rounds = run_game(game_state)
        total_rounds += rounds

        results['games_played'] += 1
        results['wins'][winner] += 1

        for card_class in Card.__subclasses__() + Treasure.__subclasses__():
            results['card_play_counts'][card_class.__name__] += card_class.played_count

            #reset card counts
            card_class.played_count = 0

        for player, score in game_state.get_scores().items():
            results['scores'][player].append(score)

        results['avg_rounds'] = total_rounds / num_games
            
    return results