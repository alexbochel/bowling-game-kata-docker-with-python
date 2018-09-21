import unittest
from bowling import BowlingGame

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.bowling_game = BowlingGame()

    def test_gutter_game(self):
        #Arrange
        expected_score = 0
        
        #Act
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        self.bowling_game.roll(0)
        
        #Assert
        self.assertEqual(self.bowling_game.score, expected_score)

if __name__ == '__main__':
    unittest.main()