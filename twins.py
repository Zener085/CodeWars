"""https://codeforces.com/problemset/problem/160/A?locale=en 900"""


def divide_coins(n: int) -> int:
    coins = sorted(list(map(int, input().split())))
    my_part, num_of_coins, total = 0, 0, sum(coins)

    for coin in reversed(coins):
        my_part += coin
        num_of_coins += 1
        if my_part > total / 2:
            return num_of_coins


print(divide_coins(int(input())))
