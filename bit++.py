"""https://codeforces.com/problemset/problem/282/A 800"""


def calculate_x(n: int) -> int:
    x = 0
    for i in range(n):
        operation = input().split("X")
        if operation[0] == "++" or operation[1] == "++":
            x += 1
        else:
            x -= 1

    return x


print(calculate_x(int(input())))
