import unittest
from typing import * 
from random import randint

import sys
import os
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(project_root, '..')))

from src.Game import Game
from src.State import State

# TODO do tests with differing numbers of players
class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.state = self.game.init_state()
        self.players = self.game.init_players(self.state)

    def test_initialize_hands(self):
        # Test initialization with default number of players
        state = self.game.init_state()
        players = self.game.init_players(state)
        state.initialize_hands()
        
        # checks that hands are correct length
        for player in players:
            self.assertEqual(len(state.hands[player]), 6)
            
        # checks that each card is, in fact, a card
        # print(f"ALL PLAYERS: {players}")
        hands = state.hands
        # print(hands)
        # find out who has the lowest trump card in their hand
        attacker = players[0]
        lowest_trump = 15
        trump_suit = state.trump_suit
        for player, hand in hands.items():
            for card in hand:
                if (card[1] == trump_suit) and (card[0] < lowest_trump):
                    lowest_trump = card[0]
                    attacker = player
                self.assertIsInstance(card, Tuple)

        # checks that the attacker, defender, and second_attacker were set correctly
        player_roles = state.get_player_roles()
        attacker_index = players.index(attacker)
        self.assertEqual(player_roles['attacker'], attacker)
        self.assertEqual(player_roles['defender'], players[(attacker_index + 1) % len(players)])
        if len(players) > 2:
            self.assertEqual(player_roles['second_attacker'], players[(attacker_index + 2) % len(players)])


    def test_draw_cards(self):
        # TODO doesn't work with num_players > 3 because others is generated when taker_takes
        game = Game(num_players_arg=4)
        state = game.init_state()
        players = game.init_players(state)
        hand = state.hands
        state.initialize_hands()

        # generates between 0 and 6 random cards
        def generate_0_to_6_cards(suits):
            return [(randint(6,15), suits[randint(0,3)]) for _ in range(0, 2)]

        # sets each player's hand to a random hand with between 0 and 6 cards
        for player in players:
            state.hands[player] = generate_0_to_6_cards(game.SUITS)

        # each player draws their cards
        state.draw_cards()
        
        # checks that each player's hand is the correct length
        for hand in state.hands.values():
            self.assertEqual(len(hand), 6)


if __name__ == '__main__':
    unittest.main()