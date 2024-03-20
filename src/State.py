from typing import *
from Player import Player

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
        self.player_roles = {'attacker': None, 'second_attacker': None, 'defender': None}

        

    def deal_cards(self):
        """draws cards til 6 for each player"""
        for player in self.players:
            while (len(self.hands[player]) < 6):
                self.hands[player].append(self.deck.pop())
        
    
    def set_players(self, players_arg: List[Player]):
        """
        Sets self.players to players_arg
        FROM GAME CLASS
        
        Param: 
        players_arg: List[Player]
        """
        self.players = players_arg
        for player in players:
            self.hands[player] = None
        

    def set_player_roles(self):
        if (self.player_roles['attacker'] == None): #start of game, picks attacker with the lowest trump card
            pass
        else:
            pass


                
    def draw_cards(self):
        """draws cards til 6 for each player"""
        for player in self.players:
            while (len(self.hands[player]) < 6):
                self.hands[player].append(self.deck.pop())


    def get_stage(self) -> Player:
        #TODO
        pass


    def reset_floor():
        #TODO
        pass
        self.players = []
    
        
