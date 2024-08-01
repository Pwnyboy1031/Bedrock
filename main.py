import game.game_logic as game_logic
from game.game_logic import take_turn


        
def main():
    game_state = game_logic.initialize_game()
    while game_state.game_over == False:
        take_turn(game_state)
    
  



if __name__ == "__main__":
    main()


   