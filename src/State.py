from typing import *
from .Player import Player

card = Tuple[int, str]
deck_type = List[card]


class State():
    def __init__(self, deck: deck_type, trump: card):
        self.deck = deck
        self.trump = trump
        self.trump_suit = trump[1]
        self.floor = []
        self.hands = {} #key: player, value: list of cards
        self.players = []   #queue, 0: attacker, 1:defender, 2:second_attacker(players>2), [3:]:others(players>3)
        self.player_roles = {'attacker': None, 'second_attacker': None, 'defender': None, 'others': []}
        
        self.durak = []
        
        self.status = {
            'game_finished': False,
            'draw': False,
            
            'turn_done': False,
            'defender_took': False,
            
            'attacker_done': False,
            'second_attacker_turn': False,
            'second_attacker_done': False,
            'attacker_left': False,
        }

        # TODO merge deal and draw
        
        self.initialize_hands()
        

    """INIT METHODS (run once)"""
    def initialize_hands(self):
        """draws cards til 6 for each player"""
        first_player = self.players[0]
        lowest_trump = 15
        
        # gives each player their hand
        for player in self.players:
            self.hands[player] = []
            while len(self.hands[player]) < 6:
                new_card = self.deck.pop()
                if (new_card[1] == self.trump_suit) and (new_card[0] < lowest_trump):
                    first_player = player
                    lowest_trump = new_card[0]
                self.hands[player].append(new_card)
        
        if lowest_trump == 15: #unlucky draw, nobody got first card, player is random
            first_player = self.players[0]
        
        #sets the queue up, attacker is first, they have lowest trump
        while (first_player != self.players[0]):
            self.players.append(self.players.pop(0))
            
        self.player_roles['attacker'] = self.players[0]
        self.player_roles['defender'] = self.players[1]
        if (len(self.players) > 2):
            self.player_roles['second_attacker'] = self.players[2]


    def set_players(self, players_arg: List[Player]): # only at the beginning
        """
        Sets self.players to players_arg
        FROM GAME CLASS
        
        Param: 
        players_arg: List[Player]
        """
        self.players = players_arg
    
    
    """GETTERS AND SETTERS"""
    def get_player_roles(self):
        """Returns the player_roles dictionary"""
        return self.player_roles
    
    
    def get_floor(self):
        """Returns the floor"""
        return self.floor
    
    def get_status(self):
        return self.status
    
    
    def get_trump(self):
        return self.trump
    
    
    def get_trump_suit(self):
        return self.trump_suit
    
    
    def set_player_hand(self, player: Player, hand: deck_type):
        self.hands[player] = hand


    """DRAW CARDS"""
            
    def draw(self, player):
        while (len(self.hands[player]) < 6 and len(self.deck) > 0):
            self.hands[player].append(self.deck.pop())
            
    def draw_cards(self):
        """draws cards til 6 for each player in order"""
        
        self.draw(self.player_roles['attacker'])
        
        if len(self.players) > 2:
            self.draw(self.player_roles['second_attacker'])
        
        # TODO needs to make sure that they're self.drawing in the order that they gave the cards to the defender
        others = self.player_roles['others']
        
        for player in others:
            if player != None:
                self.draw(player)
            
        self.draw(self.player_roles['defender'])


    def get_stage(self) -> Player:
        return self.player_roles['attacker'], self.player_roles['secondary_attacker'], self.player_roles['defender']


    def reset_floor(self): #resets floor, draws cards, sets new roles, and returns state
        
        self.floor = []
        
        #draws cards to 6
        self.draw_cards()
        
        # why are you making a function inside of this function that won't ever be used more than once?
        # TODO get rid of the function declaration and calling unless I get a good reason
        def set_player_roles():
            #preserve the queue, append to end and pop from front
            #attacker moves to back
            if not self.status['attacker_left']:
                self.players.append(self.players.pop(0))
            
            if (self.status['defender_took']): #skips their turn, defender moves to back
                self.players.append(self.players.pop(0))
            
            #new roles
            self.player_roles['attacker'] = self.players[0]
            self.player_roles['defender'] = self.players[1]
            if (len(self.players) > 2):
                self.player_roles['second attacker'] = self.players[2]

        set_player_roles()
        
        #check win conditions
        
        return self
    
    
    def game_over(self):
        if self.status['game_finished'] == True:
            self.status['draw'] = True
        else:
            self.status['game_finished'] = True
        
        
    def game_not_over(self):
        return self.status['game_finished']
    
    
    def kick_player(self, player):
        #ensures set_player_roles() in reset_floor() doesn't skip a player when setting roles
        if self.player_roles['attacker'] == player:
            self.status['attacker_left'] = True
        
        self.durak.append(player)
        self.players.remove(player)
        self.hands.pop(player)
        
        if len(self.players) == 1:
            self.game_over()
            #in the game logic the next player might end up going even if the game is over, say if a defender is going next, but this is required in case
            #there are draws
    
        """
        
        everytime a player leaves, we should check to see if the game is over since that's the only time the game would ever be over. 
        We're going to need to find a way to check for draws, also. 
        
        A game is a draw when 
        """