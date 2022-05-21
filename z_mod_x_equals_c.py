"""https://codeforces.com/contest/1684/problem/B"""


def find_xyz(a: int, b: int, c: int):
    z = c
    y = z + b
    x = y + a

    return [x, y, z]


for i in range(int(input())):
    print(*find_xyz(*map(int, input().split())))
