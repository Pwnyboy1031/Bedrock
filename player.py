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
            print(f"{index + 1}.  {card.name} - {card.effect}")
        print()
    
    def display_hoard(self):
        print(f"{self.name}'s hoard:")
        for index, card in enumerate(self.hoard):
            print(f"{index + 1}. {card.name}")