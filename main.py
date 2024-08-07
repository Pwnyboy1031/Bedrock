import game.game_logic as game_logic
from game.game_logic import take_turn
import json
from game.simulator import run_simulation

def save_results_to_file(results, filename="simulation_results.json"):
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)
        
def main():
 #   game_state = game_logic.initialize_game()
  #  while game_state.game_over == False:
    #    take_turn(game_state)

    num_simulations = 1000
    results = run_simulation(num_simulations)
    save_results_to_file(results)
    print(f"Simulation completed. Results saved to simulation_results.json")
  



if __name__ == "__main__":
    main()


   