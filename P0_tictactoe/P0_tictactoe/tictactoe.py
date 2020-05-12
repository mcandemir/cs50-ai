"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_of_X = 0
    num_of_O = 0
    for row in board:
        for cell in row:
            if cell == X:
                num_of_X += 1
            elif cell == O:
                num_of_O += 1

    if num_of_X > num_of_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action.add((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action
    if terminal(board):
        raise Exception("Game over")
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")

    current_player = player(board)
    board_copy = deepcopy(board)
    board_copy[i][j] = current_player
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # rows
    if board[0][0] == board[0][1] == board[0][2] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != EMPTY:
        return board[2][0]

    # columns
    if board[0][0] == board[1][0] == board[2][0] != EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != EMPTY:
        return board[0][2]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for row in board:
        if row.count(EMPTY) > 0:
            return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    thewinner = winner(board)
    if thewinner == X:
        return 1
    elif thewinner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return (0,0)

    current_player = player(board)

    if current_player == O:
        v = 99
        for action in actions(board):
            returned_maxvalue = maxvalue(result(board, action))
            if v > returned_maxvalue:
                v = returned_maxvalue
                move = action

    elif current_player == X:
        v = -99
        for action in actions(board):
            returned_minvalue = minvalue(result(board, action))
            if v < returned_minvalue:
                v = returned_minvalue
                move = action

    return move


def minvalue(board):
    if terminal(board):
        return utility(board)
    v = 99
    for action in actions(board):
        v = min(v, maxvalue(result(board,action)))
    return v

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -99
    for action in actions(board):
        v = max(v, minvalue(result(board,action)))
    return v