# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_alpha_beta_tic_tac_toe_agent.py

import unittest
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
        agent = AlphaBetaTicTacToeAgent(None, None)
        agent.action(('X', None, None, None, None, None, None, None, None))

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
