from .Game import Game

game = Game()
state = game.init_state()
players = game.init_players(state)
state.deal_cards()
j=1

#we need to put this into game class
while(True): #stops when one player remaining
    #One Turn
    att, att2, deff = state.get_stage() #gets players for a given turn
    
    while(Turn): #while a turn is happening
        state = att.get_move(state)
        state = deff.get_move(state)
        
        while (not state.changed?):
            state = att.get_move(state)
            state = deff.get_move(state)
        
        while (not state.changed?):
            state = att2.get_move(state)
            state = deff.get_move(state)
        
        
        state = state.reset_floor() #draws, sets new players, disqualifies no card idiots

end of game