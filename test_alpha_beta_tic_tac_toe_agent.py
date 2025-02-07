# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_alpha_beta_tic_tac_toe_agent.py

import unittest
from unittest.mock import Mock
import time
from alpha_beta_tic_tac_toe_agent import AlphaBetaTicTacToeAgent

class TestAlphaBetaTicTacToeAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        An AlphaBetaTicTacToeAgent exists.
        """
        try:
            AlphaBetaTicTacToeAgent(None, None)
        except NameError:
            self.fail("Could not instantiate AlphaBetaTicTacToeAgent")

    """
    Properties
    """

    def test_game(self):
        """
        An AlphaBetaTicTacToeAgent has a `game` property.
        """
        agent = AlphaBetaTicTacToeAgent("Fake Game", None)
        self.assertEqual("Fake Game", agent.game)

    def test_symbol(self):
        """
        An AlphaBetaTicTacToeAgent has a `symbol` property.
        """
        agent = AlphaBetaTicTacToeAgent(None, 'O')
        self.assertEqual('O', agent.symbol)

    """
    Agent Function
    """

    def test_action(self):
        """
        An AlphaBetaTicTacToeAgent has an agent function.
        """
        # Set up the mock game object
        mock_game = Mock()
        states_counter = [0]

        def is_terminal_side_effect(state):
            states_counter[0] += 1
            return states_counter[0] > 2

        mock_game.is_terminal.side_effect = is_terminal_side_effect
        mock_game.actions.return_value = [1, 2, 3, 4, 5, 6, 7, 8]
        mock_game.result.side_effect = lambda state, move: state[:move] + ('X',) + state[move+1:]
        mock_game.utility.return_value = 0
        
        agent = AlphaBetaTicTacToeAgent(mock_game, 'X')
        agent.action((None, None, None, None, None, None, None, None, None))

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
