import sys
from players.ai_player import AIPlayer
from players.ai_player_level_1 import AI_Player_Level_1
from players.player import Player
from game.deck import Deck
from game.game_state import GameState
from cards.treasure_cards import Treasure
from cards.hard_hat_card import Hard_Hat
from cards.cards import Bedrock



def draw_card(game_state):
    if not game_state.deck.cards:
        for card in game_state.discard_pile:
            game_state.deck.add_card_to_top(card)
        game_state.discard_pile.clear()
        game_state.deck.shuffle()
    if not game_state.deck.cards:
        game_state.game_over = True
        return
    card = game_state.deck.draw_card()
    if not isinstance(game_state.current_player(), AIPlayer):
        print(game_state.current_player().name,"drew:", card.name)
    else:
        print(f"{game_state.current_player().name} drew a card")
    if card.name == "Bedrock":
        card.apply_effect(game_state)
    else:
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
            print("Current hand:", [c.name for c in game_state.current_player().hand])
        

def deal_starting_hands(game_state):
    num_cards_to_draw = 5  # Example number of starting cards

    for player in game_state.players:
        starting_hand = []
        while len(starting_hand) < num_cards_to_draw:
            card = game_state.deck.draw_card()  # Assuming a method to draw a card

            if isinstance(card, Bedrock):
                # Handle bedrock card by putting it back into the deck
                game_state.deck.add_card_to_top(card)
                game_state.deck.shuffle()
            else:
                starting_hand.append(card)

        player.hand = starting_hand  # Assign the valid starting hand




def initialize_game():
    # Define players
    #player1 = Player("Taylor")
    player1 = AI_Player_Level_1("Player 1")
    player2 = AIPlayer("Player 2")
    player3 = AIPlayer("Player 3")
    player4 = AIPlayer("Player 4")
    players = [player1, player2, player3, player4]

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
        if not isinstance(player, AIPlayer):
            player.display_hand()
        print(f"{game_state.phase} Phase")
        if not isinstance(player, AIPlayer):
            print("Enter selection for 1 card or 'selection, selection' for 2 cards.")
        if game_state.phase == "Treasure":
            user_selection = player.make_decision("choose_treasure_in_hand")
        elif game_state.phase == "Main":
            user_selection = player.make_decision("choose_action_card_in_hand", game_state)

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
    if game_state.game_over:
        return True

    # Treasure phase
    game_state.phase = game_state.phases[0]

    # Prompt user for treasure cards to play
    selected_indices = choose_cards_to_play(current_player, game_state)
    if not selected_indices:
        print("No cards selected. Moving to Main phase")
        game_state.phase = game_state.phases[1]
    else: 
        selected_cards = [current_player.hand[index] for index in selected_indices]
        play_cards(game_state, selected_cards)
        game_state.phase = game_state.phases[1]
    if game_state.game_over:
        return True

    selected_indices = choose_cards_to_play(current_player, game_state)
    # Main Phase
    # Prompt user for non-treasure cards to play
    if not selected_indices:
        print("No cards selected. Ending turn")
    else: 
        selected_cards = [current_player.hand[index] for index in selected_indices]
        play_cards(game_state, selected_cards)
    if game_state.game_over:
        return True
        

    game_state.next_turn()
    print()
    game_state.display_discard_pile()
    
    return False

def game_over(game_state):
    # Update the scoreboard based on the current state
    game_state.update_scoreboard()
    scores = game_state.get_scores()
    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]

    # Check for a tie
    if len(winners) > 1:
        # Check if the deck is empty to prevent further play
        if not game_state.deck.cards:
            print("Tie detected and no cards left in the deck. The game ends in a tie.")
            game_state.game_over = True  # Explicitly set game over
            return "Tie", max_score

        print("Tie detected. Resolving tie.")

        # Shuffle discard pile back into the deck and add an extra Bedrock card
        bedrock_card = Bedrock()

        # Add discard pile back to the deck
        game_state.deck.cards.extend(game_state.discard_pile)
        game_state.discard_pile = []

        # Add an extra Bedrock card
        game_state.deck.add_card_to_top(bedrock_card)
        game_state.deck.shuffle()

        # Reset the game state for tie-breaker
        game_state.game_over = False
        game_state.bedrock_count = 0

        # Reset scores if needed
        game_state.update_scoreboard()

        print("Starting tie-breaker round.")
        return None

    else:
        # If there is a clear winner
        winner = winners[0]
        winner_score = scores[winner]
        print(f"The winner is {winner} with a score of {winner_score}!")
        game_state.game_over = True  # Mark the game as complete
        return winner, winner_score



