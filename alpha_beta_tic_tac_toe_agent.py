# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# Calvin Evans
# Inspiration taken from Fox J. Tic Tac Toe: Understanding the Minimax Algorithm from 
# www.neverstopbuilding.com

import unittest

class AlphaBetaTicTacToeAgent:

    def __init__(self, game, symbol):
        self.game = game
        self.symbol = symbol
        self.opponent = 'O' if symbol == 'X' else 'X'

    def action(self, state):
        """
        Determines the best action to take in the current state using the Alpha-Beta Pruning algorithm.
        """
        if self.game.is_terminal(state):
            # If the game is already in a terminal state, return None
            return None
        
        best_score = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        for move in self.game.actions(state):
            if state[move] is not None:
                continue
            next_state = self.game.result(state, move)
            score = self.alphabeta(next_state, self.opponent, alpha, beta)
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
        return best_move

    def alphabeta(self, state, player, alpha, beta):
        """
        Executes the Alpha-Beta Pruning algorithm to determine the optimal score for the given state.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol)

        if player == self.symbol:
            return self.max_value(state, alpha, beta)
        else:
            return self.min_value(state, alpha, beta)

    def max_value(self, state, alpha, beta):
        """
        Calculates the maximum value achievable from the given state by maximizing the agent's chances of winning.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol)

        v = float('-inf')
        for move in self.game.actions(state):
            next_state = self.game.result(state, move)
            v = max(v, self.alphabeta(next_state, self.opponent, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta):
        """
        Calculates the minimum value achievable from the given state by minimizing the opponent's chances of winning.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol)

        v = float('inf')
        for move in self.game.actions(state):
            next_state = self.game.result(state, move)
            v = min(v, self.alphabeta(next_state, self.symbol, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
