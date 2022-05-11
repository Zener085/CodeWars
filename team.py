"""https://codeforces.com/problemset/problem/231/A 800"""


def possible_solutions(n: int) -> int:
    res = 0
    for i in range(n):
        check = input().count('1')
        if check >= 2:
            res += 1

    return res


print(possible_solutions(int(input())))
