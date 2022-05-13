"""https://codeforces.com/problemset/problem/1359/A 1000"""

from math import ceil


def max_points(n: int, m: int, k: int) -> int:
    if m < n // k:
        return m

    max_jokers = n // k
    other_jokers = m - max_jokers
    one_hand_other_jokers = ceil(other_jokers / (k - 1))

    return max_jokers - one_hand_other_jokers


for i in range(int(input())):
    print(max_points(*list(map(int, input().split()))))
