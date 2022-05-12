"""https://codeforces.com/problemset/problem/306/A 800"""

from math import ceil


def divide_candies(candies: int, friends: int) -> list[int]:
    diff = ceil(candies / friends) * friends - candies
    return [candies // friends] * diff + [ceil(candies / friends)] * (friends - diff)


print(*divide_candies(*list(map(int, input().split()))))
