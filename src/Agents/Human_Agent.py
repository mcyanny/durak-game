import Player

class Human_Agent(Player):
    def prompt_agent(self, viable_cards_arg, state_arg):
        me = self.get_self()
        player_roles = state_arg.get_player_roles()
        
        if player_roles['attacker'] == me or player_roles['second_attacker'] == me:
            prompt = f"Attacker {me.get_name()}, you have {len(viable_cards_arg)} cards to choose from."
        elif player_roles['defender'] == me:
            prompt = f"Defender {me.get_name()}, you have {len(viable_cards_arg)} cards to choose from."
        else:
            raise ValueError("Agent prompted when not an attacker or defender.")
        
        card_number = input(f"What card would you like to choose?\n{list(enumerate(viable_cards_arg))}\t")
        # get the card, alter the state accordingly
    
    
    def prompt_human(self, prompt_message, error_message):
        pass