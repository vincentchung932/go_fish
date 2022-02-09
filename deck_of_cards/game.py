from classes.card import *
import random
from classes.deck import *
from classes.player import *



player1 = Player("aden",[])
player2 = Player("Nick",[])

deck1 = Deck()

player1.draw(deck1)
print(player1.hand)
print(player1.name)
player2.draw(deck1)
print(player2.hand)
print(player2.name)
