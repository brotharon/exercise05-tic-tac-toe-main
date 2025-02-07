# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_minimax_tic_tac_toe_agent

import unittest
from unittest.mock import Mock
import time
from minimax_tic_tac_toe_agent import MinimaxTicTacToeAgent


class TestMinimaxTicTacToeAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A MinimaxTicTacToeAgent exists.
        """
        try:
            MinimaxTicTacToeAgent(None, None)
        except NameError:
            self.fail("Could not instantiate MinimaxTicTacToeAgent")

    """
    Properties
    """

    def test_game(self):
        """
        A MinimaxTicTacToeAgent has a `game` property.
        """
        agent = MinimaxTicTacToeAgent("Fake Game", None)
        self.assertEqual("Fake Game", agent.game)

    def test_symbol(self):
        """
        A MinimaxTicTacToeAgent has a `symbol` property.
        """
        agent = MinimaxTicTacToeAgent(None, 'O')
        self.assertEqual('O', agent.symbol)

    """
    Agent Function
    """

    def test_action(self):
        """
        A MinimaxTicTacToeAgent has an agent function.
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
        
        agent = MinimaxTicTacToeAgent(mock_game, 'X')
        agent.action((None, None, None, None, None, None, None, None, None))



def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
