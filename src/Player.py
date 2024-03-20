from State import State

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


    def generate_attack_conditions(self, state):
        floor = self.get_floor()
        if floor:
            me = self.get_self()
            hand = state.get_player_hand(self)

            # grab player's cards, grab everything in the floor, see what cards the player has that have the same value as the cards in the 
            pass
        else:
            pass


    def generate_defense_conditions(self, state):
        pass


    def get_self(self):
        """Returns self"""
        return self
    

