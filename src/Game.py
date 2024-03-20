from State import State
from random import shuffle
from typing import *


card = Tuple[int, str]
deck_type = List[card]


class Game:
    def __init__(self, num_players_arg: int = None,
                 SUITS: Tuple[str] = ('♥', '♦', '♣', '♠'),
                 CARDS_PER_HAND: int = 6,
                 CARD_MIN_MAX: Tuple[int, int] = (6, 15),  # Fixed the variable name here
                 PLAYERS_MIN_MAX: Tuple[int, int] = (2, 5),
                 num_players = 2):

        self.SUITS = SUITS
        self.CARDS_PER_HAND = CARDS_PER_HAND
        self.CARD_MIN_MAX = CARD_MIN_MAX
        self.PLAYERS_MIN_MAX = PLAYERS_MIN_MAX
        self.num_players = num_players

        self.states_tree = None # TODO implement later.

        self.generate_deck() # sets self.deck to a deck_type


    def init_state(self):
        trump = self.deck[0]  # Assigning the trump properly
        
        state = State(self.deck, trump)
        return state


    def init_players(self, state):
        # TODO initialize the players
        for player in range(self.num_players):
            pass


    def generate_deck(self):
        """Generates a deck: List[Tuple[int, str]]"""
        self.deck = [(value, suit) for value in 
                     range(self.CARD_MIN_MAX[0], self.CARD_MIN_MAX[1]) 
                     for suit in self.SUITS]
        shuffle(self.deck) # Shuffles self.deck in place

