from colorama import init, Fore, Style
from treasure_cards import *

init()
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hoard = []
    
    def add_card_to_hand(self, card):
        self.hand.append(card)
    
    def play_card(self, card_index):
        return self.hand.pop(card_index)
    
    def display_hand(self):
        print(f"{self.name}'s hand:")
        for index, card in enumerate(self.hand):
            color = self.get_card_color(card)
            print(f"{index + 1}.  {color}{card.name}{Style.RESET_ALL} - {card.effect}")
        print()
    
    def display_hoard(self):
        print(f"{self.name}'s hoard:")
        for index, card in enumerate(self.hoard):
            color = self.get_card_color(card)
            print(f"{index + 1}. {color}{card.name}{Style.RESET_ALL}")
    
    def get_card_color(self, card):
        if isinstance(card, Ruby):
            return Fore.RED + Style.BRIGHT
        if isinstance(card, Sapphire):
            return Fore.BLUE + Style.BRIGHT
        if isinstance(card, Emerald):
            return Fore.GREEN + Style.BRIGHT
        if isinstance(card, Diamond):
            return Fore.CYAN + Style.BRIGHT
        else:
            return Fore.WHITE + Style.BRIGHT