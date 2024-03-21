import unittest
from src.Game import Game
from src.State import State
from src.Player import Player

class TestGame(unittest.TestCase):
    def set_up(self):
        self.game = Game()

    def test_generate_deck(self):
        # Test initialization to ensure deck length and trump are correct.
        game = Game()
        self.assertEqual(len(game.deck), 36)
        self.assertEqual(game.deck[0], game.deck[0])


    def test_state_init(self):
        # Ensures that the initial state generated from game contains expected values
        self.state = self.game.init_state()
        self.assertEqual(self.state.deck, self.game.deck)
        self.assertEqual(self.state.trump, self.game.deck[0])
        self.assertEqual(self.state.trump_suit, self.game.deck[0][1])
        self.assertEqual(self.state.get_floor(), [])
        self.assertEqual(self.state.hands, {})
        self.assertEqual(self.state.players, [])
        self.assertIsNone(self.state.player_roles['attacker'])
        self.assertIsNone(self.state.player_roles['second_attacker'])
        self.assertIsNone(self.state.player_roles['defender'])


    def test_players_init(self):
        # Ensures that each player generated is a Player object
        players = self.game.init_players(self.state)
        for player in players:
            self.assertIsInstance(player, Player)


if __name__ == '__main__':
    unittest.main()