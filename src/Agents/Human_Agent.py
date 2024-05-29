from ..Player import Player

class Human_Agent(Player):
    def prompt_agent_card(self, viable_cards_arg, state_arg):
        num_viable_cards = len(viable_cards_arg)
        
        me = self.get_self()
        my_name = self.name
        player_roles = state_arg.get_player_roles()
        role = "Defender" if player_roles['defender'] == me else "Attacker"
        
        condition = self.human_card_condition_generator(num_viable_cards)
        print(f"{role} {my_name}, you have {num_viable_cards} cards to choose from.")
        
        try:
            error_message = "You messed something up, input was invalid. Try again."
            prompt = f"What card would you like to choose?\n{list(enumerate(viable_cards_arg))}\t"
            user_input = self.prompt_human(prompt, error_message, num_viable_cards)
            chosen_card = viable_cards_arg(int(user_input)) if user_input.isnumeric() else user_input if user_input == 'n' else float('inf')
        except Exception as e: #did this high but think it's funny asf so it's gonna stay
            raise ValueError(f"Human user {my_name} gave invalid input resulting in {e}")
        
        return chosen_card
    
    
    def prompt_agent_giving(self, viable_cards_arg, state_arg):
        num_viable_cards = len(viable_cards_arg)
        
        prompt_message = f"Which cards would you like to give to the defender? \
        Separate your answers with commas.\n{list(enumerate(viable_cards_arg))}\t"
        error_message = f"You messed something up, input was invalid. Try again."
        condition = self.human_gives_condition_generator(num_viable_cards)
        raw_input = self.prompt_human(prompt_message, error_message, condition)
        cards = [viable_cards_arg[int(inp.strip())] for inp in raw_input.split(',')]
        return cards
    
    
    def human_card_condition_generator(self, num_viable_cards):
        def condition(self, user_input): #checks that human input is consistent with available options
            user_input = int(user_input)
            if user_input < num_viable_cards and user_input >= 0 or user_input == 'n':
                return True
            else:
                return False
        return condition


    def human_gives_condition_generator(self, num_viable_cards):
        def condition(self, user_input):
            if user_input == 'n':
                return True
            
            split = [int(inp.strip()) for inp in user_input.split(',')]
            for value in split:
                if value > num_viable_cards or value < 0:
                    return False
            return True
        return condition
        
        
    def prompt_human(self, prompt_message, error_message, condition):
        attempts = 0
        while attempts <= 10:
            try:
                user_input = input(prompt_message)
                if condition(user_input):
                    return user_input
                else:
                    print(error_message)
            except Exception as e:
                print(f"Error message: {error_message} - Error: {e}")