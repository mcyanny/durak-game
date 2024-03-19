from random import shuffle
from typing import Tuple

class Game:
    def __init__(self, num_players_arg: int = None,
                 SUITS: Tuple[str] = ('♥', '♦', '♣', '♠'),
                 CARDS_PER_HAND: int = 6,
                 CARD_MIN_MAX: Tuple[int, int] = (6, 15),  # Fixed the variable name here
                 PLAYERS_MIN_MAX: Tuple[int, int] = (2, 5)):

        self.deck = [(value, suit) for value in 
                     range(CARD_MIN_MAX[0], CARD_MIN_MAX[1]) 
                     for suit in SUITS]

        shuffle(self.deck)  # Shuffling the deck properly
        
        
        
        

    
    def initState(self):
        trump = self.deck[0]  # Assigning the trump properly
        state = State(deck, trump, players)

