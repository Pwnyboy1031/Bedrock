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

    

def resolve_effects(game_state):
    #resolution of effects after playing cards?
    pass