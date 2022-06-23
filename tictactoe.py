"""
Tic Tac Toe Player
"""

import math
import copy

from numpy import Infinity

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
    #if the game is new it is Xs turn
    if board == initial_state():
        return X

    #we iterate through the board to count how many 'X' and 'O' placements there are to determine whose turn it is after the initial turn
    xPlacements = 0
    oPlacements = 0

    for row in board:
        xPlacements += row.count(X)
        oPlacements += row.count(O)
    
    if oPlacements >= xPlacements:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = []
    #iterate throughout the board and return any positions that are available
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != X and board[i][j] != O:
                possible_action.append((i,j))
    return possible_action



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #check to see if the action is legal
    possible_action = actions(board)
    if action not in possible_action:
        raise Exception("Move is not possible")
    

    #create deep copy of the board to make changes
    deep_copy_board = copy.deepcopy(board)
    deep_copy_board[action[0]][action[1]] = player(board)    

    return deep_copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check to see if horizontals or verticals have three in a row
    for i in range(len(board)):
        #horizontal
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
        #vertical
        if board[0][i] == board[1][i] == board[2][i]:
            if board [0][i] == X:
                return X
            elif board[0][i] == O:
                return O

    #check if diagonals have three in a row

    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check to see if there is a winner or tie
    if winner(board) == X or winner(board) == O or actions(board) == []:
        return True

    return False



def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def find_min_max(board):

    #check to see if the board is terminal
    if terminal(board):
        return score(board)
    
    if player(board) == O:
        best_value = 1000
        for i in actions(board):
            #call a recursive to iterate through the function until a terminal board is met and assign a score
            value = find_min_max(result(board, i))
            #check to see if the value is lower that the current best value
            if value < best_value:
                best_value = value
        return best_value

    if player(board) == X:
        best_value = -1000
        for i in actions(board):
            #call a recursive to iterate through the function until a terminal board is met and assign a score
            value = find_min_max(result(board, i))
            #check to see if the value is lower that the current best value
            if value > best_value:
                best_value = value
        return best_value

    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #check to see if terminal board
    best_move = None

    if terminal(board):
        return None

    if player(board) == X:
        best_value = -1000
        #iterate through all possible positions
        for i in actions(board):
            value = find_min_max(result(board, i))
            if value > best_value:
                best_value = value
                best_move = i

    elif player(board) == O:
        best_value = 1000
        #iterate through all possible positions
        for i in actions(board):
            value = find_min_max(result(board, i))
            if value < best_value:
                best_value = value
                best_move = i

    return best_move
    

                