from typing import *
from Player import Player

card = Tuple[int, str]
deck = List[card]

class State():
    def __init__(self, deck: deck, trump: card):
        self.deck = deck
        self.trump = trump
        self.floor = []
        self.hands = {}
        self.players = []
        self.player_roles = {'curr_attacker': None, 'second_attacker': None, 'defender': None}

    
    def set_players(self, players_arg: List[Player]):
        """
        Sets self.players to players_arg
        
        Param: 
        players_arg: List[Player]
        """
        self.players = players_arg


    def deal_cards(self):
        """
        Sets self.hands as dictionary with a Player reference as a key 
        and the player_hand as the value. Current_attacker is set to the 
        player with the lowest value trump card.
        """
        hands = {player: [] for player in self.players}
        trump_suit = self.trump[1]
        lowest_trump = (15, trump_suit)

        for _ in range(self.CARDS_PER_HAND):
            for player_num in range(1, self.num_players + 1):
                card = self.deck.pop()
                hands[player_num].append(card)
                if (card[1] == trump_suit) and (card[0] < lowest_trump):
                    lowest_trump = card
                    self.current_attacker = player_num
        self.hands = hands


    def get_stage(self) -> Player:
        pass


    def reset_floor():
        pass