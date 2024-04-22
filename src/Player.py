from copy import deepcopy

class Player():
    def __init__(self):
        pass


    def get_move(self, state, role):
        """
        takes in agent input
        checks agent input based off of current attack and role
        returns state
        """
        attempts = 0
        while attempts < 20:
            attempts += 1
            if role == 'attacker':
                viable_moves = self.get_viable_attack_cards(state)
            elif role == 'defender':
                viable_moves = self.get_viable_defense_cards(state)
            
            return self.prompt_agent(self, viable_moves, state)


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


    def prompt_agent()
    def get_self(self):
        """Returns self"""
        return self
    

