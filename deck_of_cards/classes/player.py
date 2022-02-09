import random

class Player:
    def __init__(self,name,hand) -> None:
        self.name = name
        self.hand = []
        self.score = 0
    
    def draw(self,deck):
        num = random.randint(0,len(deck.cards)-1)
        self.hand.append(deck.cards[num])
        deck.cards.pop(num)