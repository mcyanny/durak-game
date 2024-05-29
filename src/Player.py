from copy import deepcopy
from typing import *

#TODO, make generic Player parent class and have subclasses of different agent types

class Player():
    def __init__(self):
        self.name = None


    def get_name(self):
        return self.name
    
    
    def get_move(self, state, role: str):
        if state.get_status()['turn_done']: #if attacker runs out of cards and didn't go, it will be defender's turn but they won't have any attack to defend
            return state
        
        attacker = True if role == 'attacker' else False
        
        if attacker:
            viable_moves = self.get_viable_attack_cards(state)
        else:
            viable_moves = self.get_viable_defense_cards(state)

        if viable_moves:
            chosen_card = self.prompt_agent_card(self, viable_moves, state) # should be the card that they want to play, then we alter the state accordingly.
            if chosen_card != 'n': #if they chose to play a move
                state.play_move(chosen_card, self.get_self())
                return state
        if attacker: #alters state if player doesn't have available cards or chose not to play
            if state.get_status()['attacker_done'] == True:
                state.set_status_value('second_attacker_done', True)
                return state
            else:
                state.set_status_value('attacker_done', True)
                return state
        else:
            state.set_status_value('defender_took', True)
            state.set_status_value('turn_done', True)
            return state


    def give_to_defender(self, state):
        me = self.get_self()
        viable_moves = self.get_viable_attack_cards(state)
        if viable_moves:
            cards = self.prompt_agent_giving(viable_moves, state)
            if cards != 'n':
                state.player_roles['others'].append(me)
                for card in cards:
                    state.play_move(card, me)
        
        
    def prompt_agent_card(self, viable_moves_arg, state_arg): # abstract method, should be implemented separately for each agent!!! should return state modified
        """
        Should return either 'n' or a card
        """
        pass
    
    
    def prompt_agent_giving(self, viable_moves_arg, state_arg): # abstract method
        """
        Should return either 'n' or a list of cards
        """
        pass
    
    
    def get_viable_attack_cards(self, state):
        """Returns all cards in the attacker's hand that they can use in their attack

        Args:
            state (State): the current state of the game

        Returns:
            deck_type: viable attack cards
        """        
        floor = state.get_floor()
        # me = self.get_self() # use if you can't pass self to a function
        
        hand = deepcopy(state.get_player_hand(self))
        
        # checks if there's already an attack, 
        # if there is, then attacker cards are chosen accordingly
        # if there isn't, then the attacker cards are their hand
        if floor:
            attack_values = {card[0] for card in floor}
            return [card for card in hand if card[0] in attack_values]
        else:
            return hand


    def get_viable_defense_cards(self, state):
        """Get's all cards in the defender's hand that they can use in their defense

        Args:
            state (State): the current state of the game

        Returns:
            deck_type: viable defense cards
        """        
        floor = state.get_floor()
        last_attacker_card = floor[-1]
        # me = self.get_self() # use if you can't pass self to a function
        
        hand = deepcopy(state.get_player_hand(self))
        trump_suit = state.get_trump_suit()
        
        if last_attacker_card[1] == trump_suit:
            # returns all trumps of a greater value than 
            # the last_attacker_card in the defender hand
            return [card for card in hand if 
                    (card[1] == last_attacker_card[1]) and 
                    (card[0] > last_attacker_card[0])]
        else:
            # returns all trumps and same suit higher value cards than 
            # last_attacker_card in defender hand
            return [card for card in hand if 
                    (card[1] == trump_suit) or 
                    (card[1] == last_attacker_card[1] and 
                     card[0] > last_attacker_card[0])]


    def get_self(self):
        """Returns self"""
        return self

