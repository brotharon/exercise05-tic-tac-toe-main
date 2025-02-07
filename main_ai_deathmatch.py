# Main
# A demonstration of two AI agents playing Tic Tac Toe using the Random and Minimax agents.
# Calvin Evans
# Inspired by and only slightly modifying the code from scratchpad.py

from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_game import IllegalTicTacToeMoveException
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer
from minimax_tic_tac_toe_agent import MinimaxTicTacToeAgent
from random_tic_tac_toe_agent import RandomTicTacToeAgent

renderer = TicTacToeBoardRenderer()
game = TicTacToeGame((None, None, None, None, None, None, None, None, None), renderer)
ai_agent_1 = MinimaxTicTacToeAgent(game, TicTacToeGame.P1_SYMBOL)
ai_agent_2 = RandomTicTacToeAgent(game, TicTacToeGame.P2_SYMBOL)

print(f"Let's watch two AI agents play tic-tac-toe! Agent 1 is {ai_agent_1.symbol} and Agent 2 is {ai_agent_2.symbol}.\n")
print("0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8\n")

while game.is_not_over():
    print("----------------------------------------------")
    
    # AI Agent 1 move
    while True:
        try:
            move = ai_agent_1.action(game.state)
            game.state = game.result(game.state, move)
            break
        except IllegalTicTacToeMoveException as e:
            print(e)
            print("Agent 1, please choose a valid move.")

    print(game)
    if game.is_win(game.state, ai_agent_1.symbol):
        print('Agent 1 wins!')
        break
    
    # AI Agent 2 move
    if not game.is_terminal(game.state):
        while True:
            try:
                move = ai_agent_2.action(game.state)
                game.state = game.result(game.state, move)
                break
            except IllegalTicTacToeMoveException as e:
                print(e)
                print("Agent 2, please choose a valid move.")
                
        print(game)
        if game.is_win(game.state, ai_agent_2.symbol):
            print('Agent 2 wins!')
            break

print("Game Over")
