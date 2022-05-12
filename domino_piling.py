"""https://codeforces.com/problemset/problem/50/A 800"""


def count_domino_pieces(n: int, m: int) -> int:
    return n * m // 2


print(count_domino_pieces(*list(map(int, input().split()))))
