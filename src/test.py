import unittest
from Game import Game

class TestDurak(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_init(self):
        # Test initialization with default number of players
        game = Game()
        self.assertEqual(game.get_num_players(), 4)


    def test_player


if __name__ == '__main__':
    unittest.main()