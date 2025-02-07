import unittest
from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer

class TestTicTacToeGame(unittest.TestCase):

    def setUp(self):
        self.renderer = TicTacToeBoardRenderer()
        self.initial_state = (None, None, None, None, None, None, None, None, None)
        self.game = TicTacToeGame(self.initial_state, self.renderer)

    def test_utility_player_win(self):
        # Test when the player wins
        state = ('X', 'X', 'X', None, None, None, None, None, None)
        self.assertEqual(self.game.utility(state, 'X'), 1)
        state = ('O', 'O', 'O', None, None, None, None, None, None)
        self.assertEqual(self.game.utility(state, 'O'), 1)

    def test_utility_opponent_win(self):
        # Test when the opponent wins
        state = ('O', 'O', 'O', None, None, None, None, None, None)
        self.assertEqual(self.game.utility(state, 'X'), -1)
        state = ('X', 'X', 'X', None, None, None, None, None, None)
        self.assertEqual(self.game.utility(state, 'O'), -1)

    def test_utility_draw(self):
        # Test when it's a draw
        state = ('X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X')
        self.assertEqual(self.game.utility(state, 'X'), 0)
        self.assertEqual(self.game.utility(state, 'O'), 0)

    def test_utility_no_winner(self):
        # Test when there is no winner yet
        state = ('X', 'O', 'X', None, 'O', 'X', 'O', 'X', 'O')
        self.assertEqual(self.game.utility(state, 'X'), 0)
        self.assertEqual(self.game.utility(state, 'O'), 0)

if __name__ == '__main__':
    unittest.main()
