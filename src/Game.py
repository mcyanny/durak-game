from random import shuffle
from typing import Tuple

class Game:
    def __init__(self, num_players_arg: int = None,
                 SUITS: Tuple[str] = ('♥', '♦', '♣', '♠'),
                 CARDS_PER_HAND: int = 6,
                 CARD_MIN_MAX: Tuple[int, int] = (6, 15),  # Fixed the variable name here
                 PLAYERS_MIN_MAX: Tuple[int, int] = (2, 5)
                 num_players = 2):

        self.num_players = num_players
        

        self.deck = [(value, suit) for value in 
                     range(CARD_MIN_MAX[0], CARD_MIN_MAX[1]) 
                     for suit in SUITS]

        shuffle(self.deck)  # Shuffling the deck properly
        
        init_state()
        init_players()
    
    def init_state(self):
        trump = self.deck[0]  # Assigning the trump properly
        
        state = State(self.deck, trump)
        return state

    def init_players(self, state):
        for player in range(self.num_players):
            #determine types of agents
            
            

