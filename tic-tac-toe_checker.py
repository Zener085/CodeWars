"""https://www.codewars.com/kata/525caa5c1bf619d28c000335 5 kyu"""


def zero_checker(board: list[list]) -> bool:
    check = [False] * len(board)
    for i in range(len(board)):
        if 0 not in board[i]:
            check[i] = True

    return sum(check) == len(check)


def is_solved(board: list[list]) -> int:
    for i in board:
        if i[0] == i[1] == i[2] != 0:
            return i[0]

    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        return board[1][1]

    if zero_checker(board):
        return 0

    return -1
