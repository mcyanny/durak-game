from random import shuffle
from typing import *

class Game():
    def __init__(self, num_players_arg: int = None, 
                 SUITS: Tuple[str] = ('♥', '♦', '♣', '♠'),
                 CARDS_PER_HAND: int = 6,
                 CARDS_MIN_MAX: Tuple[int, int] = (6, 15),
                 PLAYERS_MIN_MAX: Tuple[int, int] = (2, 5)):

        deck = [(value, suit) for value in 
                range(self.CARD_MIN_MAX[0], self.CARD_MIN_MAX[1]) 
                for suit in self.SUITS]

        shuffle(deck)

        self.trump = deck[0]
        self.deck = deck
