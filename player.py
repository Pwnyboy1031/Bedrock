class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_card_to_hand(self, card):
        self.hand.append(card)
    
    def play_card(self, card_index):
        return self.hand.pop(card_index)
    
    def display_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(card.name)