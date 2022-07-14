"""
Tic Tac Toe Player
"""

from distutils.log import error
from json.encoder import INFINITY
import math
import copy

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
    rowLen = len(board)
    columnLen = len(board[0])

    xCount = 0
    oCount = 0

    for i in range(rowLen):
        for k in range(columnLen):
            if board[i][k] == X:
                xCount+=1
            elif board[i][k] == O:
                oCount+=1
    
    if xCount <= oCount:
        return X
    else:
        return O




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Find the row and column length to iterate over the game board
    rowLen = len(board)
    columnLen = len(board[0])

    possibleActions = set()

    for i in range(rowLen):
        for k in range(columnLen):
            if board[i][k] == EMPTY:
                 possibleActions.add((i,k))

    return possibleActions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    
    newBoard = copy.deepcopy(board)
    x = action[0]
    y = action[1]


    if newBoard[x][y] != EMPTY:
        raise ValueError("Please choose empty space")

    else:
        newBoard[x][y] = player(board)
    
    return newBoard


def checkWinner(player,board):
    # Checks the board to find the winner horizontally, vertically, or diagonally.

    rowLen = len(board)
    columnLen = len(board[0])
    win = None

    # Check horizontally
    for i in range(rowLen):
        win = True
        for k in range(columnLen):
            if board[i][k] != player:
                win=False
                break
        
        if win:
            return win

    # Check vertically
    for i in range(rowLen):
        win = True
        for k in range(columnLen):
            if board[k][i] != player:
                win=False
                break
        if win:
            return win
        

    # Check left diagonally
    win = True
    for i in range(rowLen):
        for k in range(columnLen):
            if(i == k):
                if board[i][k] != player:
                    win=False
                    break
    if win:
        return win

    # Check right diagonally
    win = True
    for i in range(rowLen):
        for k in range(columnLen):
            if(i + k == rowLen-1):
                if board[i][k] != player:
                    win=False
                    break

    if win:
        return win
    
    return False
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkWinner(X,board):
        return X
    elif checkWinner(O,board):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    action = actions(board)
    if(winner(board) == X or winner(board) == O or len(action) == 0):
        return True

    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X :
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maxValue(board):

    if(terminal(board)):
        return utility(board)
    
    v = float("-inf")

    for action in actions(board):
        v = max(v, minValue(result(board,action)))

    return v

def minValue(board):
    if(terminal(board)):
        return utility(board)
    
    v = float("inf")

    for action in actions(board):
        v = min(v, maxValue(result(board,action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    elif player(board) == X:
        optimalAction = None
        v = float("-inf")
        for action in actions(board):
            minValueSet = minValue(result(board,action))

            if(minValueSet > v):
                v = minValueSet
                optimalAction = action

        return optimalAction


    elif player(board) == O:
        optimalAction = None
        v = float("inf")

        for action in actions(board):
            maxValueSet = maxValue(result(board,action))

            if(maxValueSet < v):
                v = maxValueSet
                optimalAction = action

            return optimalAction



