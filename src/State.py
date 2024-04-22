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
        self.players = []
        self.player_roles = {'attacker': None, 'second_attacker': None, 'defender': None, 'others': []}

        # TODO merge deal and draw

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
        
        # TODO find a way to choose the first player without a trump, or deal again
        if lowest_trump == 15:
            raise ValueError("You got unlucky with the draw.")
        
        # sets player_roles according to who has the lowest value trump
        # card in their hand
        if len(self.players) > 2:
            attacker_index = self.players.index(first_player)
            self.player_roles['attacker'] = first_player
            self.player_roles['defender'] = self.players[(attacker_index + 1) % len(self.players)]
            self.player_roles['second_attacker'] = self.players[(attacker_index + 2) % len(self.players)]  
            
        else:
            attacker_index = self.players.index(first_player)
            self.player_roles['attacker'] = first_player
            self.player_roles['defender'] = self.players[(attacker_index + 1) % len(self.players)]


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
    
    
    def get_trump(self):
        return self.trump
    
    
    def get_trump_suit(self):
        return self.trump_suit
    
    
    def set_player_hand(self, player: Player, hand: deck_type):
        self.hands[player] = hand


    """DRAW CARDS"""
    def draw_cards(self):
        """draws cards til 6 for each player"""
        
        def draw(player):
            while (len(self.hands[player]) < 6 and len(self.deck) > 0):
                self.hands[player].append(self.deck.pop())
        
        draw(self.player_roles['attacker'])
        
        if len(self.players) > 2:
            draw(self.player_roles['second_attacker'])
        
        # TODO needs to make sure that they're drawing in the order that they gave the cards to the defender
        others = self.player_roles['others']
        
        for player in others:
            draw(player)
            
        draw(self.player_roles['defender'])


    def get_stage(self) -> Player:
        #TODO
        pass


    def reset_floor():
        #TODO
        pass