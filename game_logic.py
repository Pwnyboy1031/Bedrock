from player import Player
from deck import Deck
from game_state import GameState

def draw_card(game_state):
    card = game_state.deck.draw_card()
    game_state.current_player().add_card_to_hand(card)
    print(game_state.current_player().name,"drew:", card.name)

def play_cards(game_state, cards):
    for card in reversed(cards):
        card.apply_effect(game_state)
        try:
            card_index = game_state.current_player().hand.index(card)
            print(game_state.current_player().name, "played:", card.name)
            print(f"{card.name}'s effect says: {card.effect}")
            game_state.current_player().hand.pop(card_index)
        except ValueError:
            print("Card not found in player's hand:", card)

def deal_starting_hands(game_state):
    for _ in range(10): 
        draw_card(game_state)
        game_state.next_turn()


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

def choose_cards_to_play(player):
    player.display_hand()
    print("Options:")
    print("Enter selection for 1 card or 'selection, selection' for 2 cards.")
    user_selection = input().strip()
    if not user_selection:
        return [] # return empty list if no input
    card_indices = [int(index) - 1 for index in user_selection.split(',')]

    if len(card_indices) > 2:
        print("Invalid input. You can only play one or two cards.")
        return choose_cards_to_play(player)
    
    return card_indices

def take_turn(game_state):
    # define current player's turn from game state
    current_player = game_state.current_player()

    # Announce turn player
    print(f"It's {current_player.name}'s turn.")

    # draw card for turn player
    draw_card(game_state)

    #TO DO: Input any treasures or N for no treasures

    # Prompt user for non treasure cards to play
    selected_indices = choose_cards_to_play(current_player)
    if not selected_indices:
        print("No cards selected. Ending turn")
    else: 
        selected_cards = [current_player.hand[index] for index in selected_indices]
        play_cards(game_state, selected_cards)

    game_state.next_turn()
    take_turn(game_state)

    

def resolve_effects(game_state):
    #resolution of effects after playing cards?
    pass