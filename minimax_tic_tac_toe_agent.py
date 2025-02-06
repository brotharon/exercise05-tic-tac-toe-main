# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Calvin Evans
# Inspiration taken from Fox J. Tic Tac Toe: Understanding the Minimax Algorithm from 
# www.neverstopbuilding.com

import unittest

class MinimaxTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol
        self.opponent = 'O' if symbol == 'X' else 'X'

    def action(self, state):
        """
        Determines the best action to take in the current state using the Minimax algorithm.
        """
        if self.game.is_terminal(state):
            # If the game is already in a terminal state, return None
            return None
        
        best_score = float('-inf')
        best_move = None
        for move in self.game.actions(state):
            if state[move] is not None:
                continue
            next_state = self.game.result(state, move)
            score = self.minimax(next_state, self.opponent)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, state, player):
        """
        Executes the Minimax algorithm to determine the optimal score for the given state.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol)

        if player == self.symbol:
            return self.max_value(state)
        else:
            return self.min_value(state)

    def max_value(self, state):
        """
        Calculates the maximum value achievable from the given state by maximizing the agent's chances of winning.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol)

        v = float('-inf')
        for move in self.game.actions(state):
            next_state = self.game.result(state, move)
            v = max(v, self.minimax(next_state, self.opponent))
        return v

    def min_value(self, state):
        """
        Calculates the minimum value achievable from the given state by minimizing the opponent's chances of winning.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol)

        v = float('inf')
        for move in self.game.actions(state):
            next_state = self.game.result(state, move)
            v = min(v, self.minimax(next_state, self.symbol))
        return v
