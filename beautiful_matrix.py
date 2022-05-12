"""https://codeforces.com/problemset/problem/263/A 800"""


def make_beautiful() -> int:
    res = 0
    for i in range(5):
        row = input().split()
        if '1' in row:
            res = abs(2 - i) + abs(2 - row.index('1'))

    return res


print(make_beautiful())
