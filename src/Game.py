from random import shuffle

class Game():
    def __init__(self):
        deck = [(value, suit) for value in 
                range(self.CARD_MIN_MAX[0], self.CARD_MIN_MAX[1]) 
                for suit in self.SUITS]
        shuffle(deck)

        self.trump = deck[0]
        self.deck = deck
