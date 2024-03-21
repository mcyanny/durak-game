import unittest
from ..src.Game import Game
from ..src.State import State

class TestGame(unittest.TestCase):
    def set_up(self):
        self.game = Game()
        self.state = self.game.init_state()
        self.players = self.game.init_players(self.state)
        self.state.deal_cards()

    def test_game_init(self):
        # Test initialization with default number of players
        game = Game()
        self.assertEqual(game.get_num_players(), 4)


    def test_state_init(self):
        pass


    def test_players_init(self):
        pass


if __name__ == '__main__':
    unittest.main()