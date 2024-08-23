# A list with three lists of length 3 can represent a tic-tac-toe board

from typing import List

board: List[List[str]] = [['_'] * 3 for i in range(3)]

assert board == [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

board[1][2] = 'X'

assert board == [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']], 'Element [1,2] should be X'