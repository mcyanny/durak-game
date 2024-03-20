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
        first_player = self.players[0]
        lowest_trump = 15
        
        for player in self.players:
            self.hands[player] = []
            while len(self.hands[player]) < 6:
                new_card = self.deck.pop()
                if new_card[1] == self.trump_suit and new_card[0] < lowest_trump:
                    first_player = player
                self.hands[player].append(new_card)
        
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
    
        
