import sys
from players.ai_player import AIPlayer
from players.player import Player
from game.deck import Deck
from game.game_state import GameState
from cards.treasure_cards import Treasure
from cards.hard_hat_card import Hard_Hat


def draw_card(game_state):
    card = game_state.deck.draw_card()
    print(game_state.current_player().name,"drew:", card.name)
    if card.name == "Bedrock":
        card.apply_effect(game_state)
        return
    game_state.current_player().add_card_to_hand(card)
    


def reveal_cards(cards):
    print("Revealing cards:")
    for index, card in enumerate (cards):
        print(f"{index + 1}. {card.name}")

def add_to_hoard(game_state, player, card):
    player.hoard.append(card)
    game_state.update_scoreboard()

def remove_from_hoard(game_state, player, card):
    player.hoard.pop(card)
    game_state.update_scoreboard()

def add_to_discard_pile(game_state, card):
    game_state.discard_pile.append(card)
    
def play_cards(game_state, cards):
    for card in reversed(cards):
        try:
            card_index = game_state.current_player().hand.index(card)
            # remove from hand
            game_state.current_player().hand.pop(card_index)
            print(game_state.current_player().name, "played:", card.name)
            print(f"{card.name}'s effect says: {card.effect}")
            card.apply_effect(game_state)
            if (not isinstance(card, Treasure) and not isinstance(card, Hard_Hat)):
                add_to_discard_pile(game_state, card)
        except ValueError:
            print("Card not found in player's hand:", card)
        

def deal_starting_hands(game_state):
    for _ in range(5):
        for player in game_state.players: 
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
    player2 = AIPlayer("Player 2")
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
        return False
    return True
        
def validate_play(player, card_indices, game_state):
    if len(card_indices) > 2:
        print("Invalid input. You can play up to 2 non-treasure cards.")
        return(False)
    
    for index in card_indices:
        if index >= len(player.hand) or any(isinstance(player.hand[(index)], Treasure) for index in card_indices):
            print("Invalid input. Ensure your selections are valid, non-treasure cards.")
            print()
            return False
        return True

def validate_treasure(player, card_indices, game_state):
    if len(card_indices) > 2:
        print("Invalid input. You can play up to 2 treasure cards.")
        return False
    for index in card_indices:
        if index >= len(player.hand) or not isinstance(player.hand[index], Treasure):
            print("Invalid input. Ensure your selections are valid, treasure cards.")
            print()
            return False
    return True
    
def validate_hoard(player, card_indices):
    if len(card_indices) > len(player.hoard) or any(not isinstance(player.hoard[(index)], Treasure) for index in card_indices):
        print("Invalid selection. You can choose any number of treasures to remove from your hoard")
        return(False)
    return True

def choose_cards_to_play(player, game_state):
    while True:
        player.display_hand()
        print(f"{game_state.phase} Phase")
        print("Enter selection for 1 card or 'selection, selection' for 2 cards.")
        if game_state.phase == "Treasure":
            user_selection = player.make_decision("choose_treasure_in_hand")
        elif game_state.phase == "Main":
            user_selection = player.make_decision("choose_action_card_in_hand")

        if not user_selection:
            return [] # return empty list if no input
        card_indices = [int(index) - 1 for index in user_selection.split(',')]

        # Check turn phase
        if game_state.phase == "Treasure":
            if validate_treasure(player, card_indices, game_state):
                return card_indices
        if game_state.phase == "Main":
            if validate_play(player, card_indices, game_state):
                return card_indices



def take_turn(game_state):
    # define current player's turn from game state
    current_player = game_state.current_player()

    # Announce turn player
    print()
    print(f"It's {current_player.name}'s turn.")
    print()
    print(f"Cards left in deck: {len(game_state.deck.cards)}")

    # Show discard pile
    game_state.display_discard_pile()

    #display hoards
    for player in game_state.players:
        player.display_hoard()
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
    print()
    game_state.display_discard_pile()

def game_over(game_state):
    game_state.game_over = True
    previous_score = 0
    winner = None
    print("Game over!")
    for player in game_state.players:
        game_state.update_scoreboard()

    for player in game_state.players:
        player_score = game_state.scoreboard.get(player.name, 0)
        if player_score > previous_score:
            winner = player.name
            previous_score = player_score
        elif player_score == previous_score:
            winner = None

    if winner:
        print(f"The winner is {winner}!")
    else:
        print("Tie Game!")
    wait = input()
    sys.exit()