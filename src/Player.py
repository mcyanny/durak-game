from copy import deepcopy

#TODO, make generic Player parent class and have subclasses of different agent types

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
                move_conditions = self.generate_attack_conditions
            elif role == 'defender':
                move_conditions = self.generate_defense_conditions
            # TODO find state.roles[player], find floor, use those to determine what the proper input would be, use that to check the input
        pass


    def get_viable_attack_cards(self, state):
        """Returns the cards that a player can use"""
        floor = self.get_floor()
        me = self.get_self()
        hand = deepcopy(state.get_player_hand(self))
        if floor:
            attack_values = {card[0] for card in floor}
            return [card for card in hand if card[0] in attack_values]
        else:
            return hand


    def generate_defense_conditions(self, state):
        pass


    def get_self(self):
        """Returns self"""
        return self
    

