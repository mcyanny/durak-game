from .State import State
from .Player import Player
from .Agents import Human_Agent, Simplest_Agent
from random import shuffle
from typing import *


card = Tuple[int, str]
deck_type = List[card]

"""
events
('player_action', {'player': player_reference, 'action': card(s)/'n'})
('gives', {'player': player_reference, 'gave': card(s)/'n'})
('takes', {'player': player_reference, 'took': card(s)/'n'})
('draws', {'players': [players]})
"""

class Game:
    def __init__(self,
                 num_players_arg: int = 2,
                 SUITS: Tuple[str] = ('♥', '♦', '♣', '♠'),
                 CARDS_PER_HAND: int = 6,
                 CARD_MIN_MAX: Tuple[int, int] = (6, 15),
                 PLAYERS_MIN_MAX: Tuple[int, int] = (2, 5),
                 event_log = [],):
        self.SUITS = SUITS
        self.CARDS_PER_HAND = CARDS_PER_HAND
        self.CARD_MIN_MAX = CARD_MIN_MAX
        self.PLAYERS_MIN_MAX = PLAYERS_MIN_MAX
        
        self.num_players = num_players_arg
        self.event_log = event_log

        self.generate_deck() # sets self.deck to a full shuffled deck_type


    """INIT METHODS (run once)"""
    def init_state(self):
        """Returns the starting state of the game"""
        trump = self.deck[0]  # Assigning the trump properly
        state = State(self.deck, trump)
        return state


    def init_players(self, state):
        """Initializes the players in the game's state"""
        players = []
        players.append(Simplest_Agent())
        players.append(Human_Agent())
        # for player in range(0, self.num_players):
        #     player = Simplest_Agent()
        #     players.append(player)
        state.set_players(players)
        return state


    def generate_deck(self):
        """Generates a deck: List[Tuple[int, str]]"""
        self.deck = [(value, suit) for value in 
                        range(self.CARD_MIN_MAX[0], self.CARD_MIN_MAX[1]) 
                        for suit in self.SUITS]
        shuffle(self.deck) # Shuffles self.deck in place


    def log_event(self, event):
        self.event_log.append(event)
    
    
    """GAME LOOP"""
    def play(self):
        # sets up the initial state of the game
        state = self.init_state()
        state = self.init_players(state)
        state.initialize_hands()
        
        while(state.game_not_over()): #stops when one player remaining
            #One Turn
            att, att2, deff = state.get_stage() #gets players for a given turn
            
            state = att.get_move(state, 'attacker') #inserting role as a string feels stupid, but alternatives feel even dumber
            self.log_event(state.get_last_event())
            state = deff.get_move(state, 'defender')
            self.log_event(state.get_last_event())
            status = state.get_status()
            
            
            while (not status['turn_done'] and not status['attacker_done'] and not status['game_finished']):
                state = att.get_move(state, 'attacker')
                self.log_event(state.get_last_event())
                state = deff.get_move(state, 'defender')
                self.log_event(state.get_last_event())
                status = state.get_status()
            
            while (att2 != None and not status['turn_done'] and not status['second_attacker_done'] and not status['game_finished']):
                state = att2.get_move(state, 'attacker')
                self.log_event(state.get_last_event())
                state = deff.get_move(state, 'defender')
                self.log_event(state.get_last_event())
                status = state.get_status()
            
            # defender defends, keep going
            # defender takes
            # attacker passes
            
            # defender defends, keep going
            # defender takes
            # second passes
            
            if (status['defender_took']):
                # each player contributes what they want/can
                players = state.get_players()
                for player in players:
                    player.give_to_defender(state)
                    self.log_event(player.get_last_event())
                
                # defender takes all cards from the floor
                for card in state.get_floor():
                    state.hands[deff].append(card)
                self.log_event(('takes', {'player': deff, 'took': state.get_floor()}))
            
            state = state.reset_floor() #draws and resets
            self.log_event(state.get_last_event())
        
        status = state.get_status()
        durak = state.durak if status['draw'] else state.durak[0]
        return durak, self.event_log
