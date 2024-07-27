import sys
from player import Player
from deck import Deck
from game_state import GameState
from treasure_cards import Treasure


def draw_card(game_state):
    card = game_state.deck.draw_card()
    print(game_state.current_player().name,"drew:", card.name)
    if card.name == "Bedrock":
        card.apply_effect(game_state)
    game_state.current_player().add_card_to_hand(card)
    


def reveal_cards(cards):
    print("Revealing cards:")
    for index, card in enumerate (cards):
        print(f"{index + 1}. {card.name}")

def add_to_hoard(game_state, player, card):
    player.hoard.append(card)
    game_state.update_scoreboard(player)

def remove_from_hoard(game_state, player, card):
    player.hoard.pop(card)
    game_state.update_scoreboard(player)

def add_to_discard_pile(game_state, card):
    game_state.discard_pile.append(card)
    
def play_cards(game_state, cards):
    for card in reversed(cards):
        try:
            card_index = game_state.current_player().hand.index(card)
            print(game_state.current_player().name, "played:", card.name)
            print(f"{card.name}'s effect says: {card.effect}")
            add_to_discard_pile(game_state, card)
            # remove from hand
            game_state.current_player().hand.pop(card_index)
        except ValueError:
            print("Card not found in player's hand:", card)
        card.apply_effect(game_state)

def deal_starting_hands(game_state):
    for _ in range(10): 
        draw_card(game_state)
        game_state.next_turn()
    if game_state.bedrock_count >= 1:
        from main import main
        print("Bedrock drawn in opening hand, restarting game")
        # restart game if bedrock is drawn
        main()
        return

def initialize_game():
    # Define players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    players = [player1, player2]

    # initialize deck and shuffle
    deck = Deck()
    deck.shuffle()

    game_state = GameState(players, deck)

    # Give each player 5 cards
    deal_starting_hands(game_state)

    
    return game_state

def validate_card_in_hand(player, card_indices, game_state):
    if any(index < 0 or index >= len(player.hand) for index in card_indices):
        print("Invalid input. You selected cards not in hand")
        return choose_cards_to_play(player, game_state)
        
def validate_play(player, card_indices, game_state):
    if len(card_indices) > 2 or any(isinstance(player.hand[(index)], Treasure) for index in card_indices):
        print("Invalid input. You can play up to 2 non-treasure cards")
        return choose_cards_to_play(player, game_state)

def validate_treasure(player, card_indices, game_state):
    if len(card_indices) > 2 or any(not isinstance(player.hand[(index)], Treasure) for index in card_indices):
        print("Invalid input. You can play up to 2 treasure cards")
        return choose_cards_to_play(player, game_state)
    
def validate_hoard(player, card_indices):
    if len(card_indices) > len(player.hoard) or any(not isinstance(player.hoard[(index)], Treasure) for index in card_indices):
        print("Invalid selection. You can choose any number of treasures to remove from your hoard")
        return(False)

def choose_cards_to_play(player, game_state):
    player.display_hand()
    print(f"{game_state.phase} Phase")
    print("Enter selection for 1 card or 'selection, selection' for 2 cards.")
    user_selection = input().strip()
    if not user_selection:
        return [] # return empty list if no input
    card_indices = [int(index) - 1 for index in user_selection.split(',')]

    # Check turn phase
    if game_state.phase == "Treasure":
        validate_treasure(player, card_indices, game_state)
        return card_indices
    if game_state.phase == "Main":
        validate_play(player, card_indices, game_state)
        return card_indices



def take_turn(game_state):
    # define current player's turn from game state
    current_player = game_state.current_player()

    # Announce turn player
    print()
    print(f"It's {current_player.name}'s turn.")
    print()

    # draw card for turn player
    draw_card(game_state)

    # Treasure phase
    game_state.phase = game_state.phases[0]

    # Prompt user for treasure cards to play
    selected_indices = choose_cards_to_play(current_player, game_state)
    if not selected_indices:
        print("No cards selected. Ending turn")
        game_state.phase = game_state.phases[1]
    else: 
        selected_cards = [current_player.hand[index] for index in selected_indices]
        print(selected_cards)
        play_cards(game_state, selected_cards)
        game_state.phase = game_state.phases[1]

    selected_indices = choose_cards_to_play(current_player, game_state)
    # Main Phase
    # Prompt user for non-treasure cards to play
    if not selected_indices:
        print("No cards selected. Ending turn")
    else: 
        selected_cards = [current_player.hand[index] for index in selected_indices]
        play_cards(game_state, selected_cards)
        

    game_state.next_turn()
    print(game_state.discard_pile)

def game_over(game_state):
    game_state.game_over == True
    previous_score = 0
    print("Game over!")
    for player in game_state.players:
        game_state.update_scoreboard(player)
    for player in game_state.scoreboard:
        if game_state.scoreboard.get(player) > previous_score: 
            winner = player
        previous_score = game_state.scoreboard.get(player)
    print(f"The winner is {winner}!")
    sys.exit()