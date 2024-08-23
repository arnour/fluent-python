# A list with three references to the same list is useless

from typing import List

weird_board: List[List[str]] = [["_"] * 3] * 3

# The outer list is made of three references to the same inner list. While it is unchanged, all seems right.
assert weird_board == [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

# Placing a mark in row 1, column 2, reveals that all rows are aliases referring to the same object.
weird_board[1][2] = "O"

assert weird_board == [
    ["_", "_", "O"],
    ["_", "_", "O"],
    ["_", "_", "O"],
], "Element [1,2] of all inner lists should be O"
