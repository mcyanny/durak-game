from .State import State
from .Player import Player
from random import shuffle
from typing import *


card = Tuple[int, str]
deck_type = List[card]


class Game:
    def __init__(self, num_players_arg: int = 2,
                 SUITS: Tuple[str] = ('♥', '♦', '♣', '♠'),
                 CARDS_PER_HAND: int = 6,
                 CARD_MIN_MAX: Tuple[int, int] = (6, 15),  # Fixed the variable name here
                 PLAYERS_MIN_MAX: Tuple[int, int] = (2, 5)):

        self.SUITS = SUITS
        self.CARDS_PER_HAND = CARDS_PER_HAND
        self.CARD_MIN_MAX = CARD_MIN_MAX
        self.PLAYERS_MIN_MAX = PLAYERS_MIN_MAX
        self.num_players = num_players_arg

        self.states_tree = None # TODO implement later.

        self.generate_deck() # sets self.deck to a full shuffled deck_type


    def init_state(self):
        """Returns the starting state of the game"""
        trump = self.deck[0]  # Assigning the trump properly
        #we need to draw from the end of the deck
        state = State(self.deck, trump)
        return state


    def init_players(self, state):
        """Initializes the players in the game's state"""
        # TODO initialize the players
        players = []
        for player in range(0, self.num_players):
            player = Player()
            players.append(player)
        state.set_players(players)
        return players


    def generate_deck(self):
        """Generates a deck: List[Tuple[int, str]]"""
        self.deck = [(value, suit) for value in 
                        range(self.CARD_MIN_MAX[0], self.CARD_MIN_MAX[1]) 
                        for suit in self.SUITS]
        shuffle(self.deck) # Shuffles self.deck in place

    def play(self):
        
        state = self.init_state()
        num_players = self.init_players(state)
        
        while(True): #stops when one player remaining
            #One Turn
            att, att2, deff = state.get_stage() #gets players for a given turn
            
            state = att.get_move(state)
            state = deff.get_move(state)
            status = state.get_status()
            
            
            while (not status['turn_done'] and not status['attacker_done'] and not status['second_attacker_turn']):
                state = att.get_move(state)
                state = deff.get_move(state)
                status = state.get_status()
            
            while (att2 != None and not status['turn_done'] and not status['second_attacker_done']):
                state = att2.get_move(state)
                state = deff.get_move(state)
                status = state.get_status()
            
            # defender defends, keep going
            # defender takes
            # attacker passes
            
            # defender defends, keep going
            # defender takes
            # second passes
            
            if (status['defender_took']):
                #let each player contribute cards
                #the only place where we ask players to give cards
                pass
            
            
            state = state.reset_floor() #draws and resets
