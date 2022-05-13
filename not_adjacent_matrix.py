"""https://codeforces.com/problemset/problem/1520/C 1000"""

from typing import Union


def _change_rows(matrix: list[list[int]]) -> None:
    """change numbers in each row of matrix"""
    k = 1
    for i in range(len(matrix)):
        if i % 2:
            matrix[i].reverse()
        else:
            for j in range(k):
                matrix[i] = [matrix[i][-1]] + matrix[i][:-1]
            k += 1


def _add_numbers(matrix: list[list[int]]) -> list[list[int]]:
    """add numbers from one row of one matrix to different rows of another matrix"""
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([0] * len(matrix))

    k = 0
    for row in matrix:
        for i in range(len(matrix)):
            new_matrix[k % len(matrix)][i] = row[i]
            k += 1
        k += 1

    return new_matrix


def not_adjacent_matrix(n: int) -> Union[int, list[list[int]]]:
    """create not adjacent matrix n * n if it's possible to create"""
    if n <= 0 or n == 2:
        return -1

    num = 1
    matrix: list[list[int]] = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(num)
            num += 1
        matrix.append(row)

    _change_rows(matrix)

    return _add_numbers(matrix)


def read_console() -> None:
    """read numbers from console and print answers to it"""
    t = int(input())
    for i in range(t):
        n = int(input())
        matrix = not_adjacent_matrix(n)

        if matrix == -1:
            print(matrix)
        else:
            for row in matrix:
                print(*row)


read_console()
