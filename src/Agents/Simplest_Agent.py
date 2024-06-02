from ..Player import Player

class Simplest_Agent(Player):
    """
    Will play the first card in their hand everytime, and gives defender
    all cards that they can when prompted. 
    """
    def prompt_agent_card(self, viable_cards_arg, state_arg):
        try:
            return viable_cards_arg[0]
        except Exception as e:
            raise ValueError("Random_Agent error ig?")
        
    
    def prompt_agent_giving(self, viable_cards_arg, state_arg):
        return viable_cards_arg
    
    