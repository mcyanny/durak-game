from typing import *

card = Tuple[int, str]
deck = List[card]

class State():
    def __init__(self, deck: deck, trump: card):
        self.deck = deck
        self.trump = trump
        self.players = []
    
        