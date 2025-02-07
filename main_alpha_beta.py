# Main
# A demonstration of the MinimaxTicTacToeAgent.
# Calvin Evans
# Inspired by and only slightly modifying the code from scratchpad.py

from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_game import IllegalTicTacToeMoveException
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer
from human_tic_tac_toe_agent import HumanTicTacToeAgent
from alpha_beta_tic_tac_toe_agent import AlphaBetaTicTacToeAgent

renderer = TicTacToeBoardRenderer()
game = TicTacToeGame((None, None, None, None, None, None, None, None, None), renderer)
human_agent = HumanTicTacToeAgent(game, TicTacToeGame.P1_SYMBOL)
advanced_ai_agent = AlphaBetaTicTacToeAgent(game, TicTacToeGame.P2_SYMBOL)

print(f"Let's play tic-tac-toe! You are {human_agent.symbol} and I am {advanced_ai_agent.symbol}.\n")
print("0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8\n")

while game.is_not_over():
    print("----------------------------------------------")
    
    # Human move
    while True:
        try:
            move = human_agent.action(game.state)
            game.state = game.result(game.state, move)
            break
        except IllegalTicTacToeMoveException as e:
            print(e)
            print("Please choose a valid move.")

    print(game)
    if game.is_win(game.state, human_agent.symbol):
        print('You win!')
        break
    
    # AI move
    if not game.is_terminal(game.state):
        game.state = game.result(game.state, advanced_ai_agent.action(game.state))
        print(game)
        if game.is_win(game.state, advanced_ai_agent.symbol):
            print('I win!')
            break

print("Game Over")
