"""https://codeforces.com/problemset/problem/339/A 800"""


def make_easier() -> str:
    nums = input().split('+')

    return "+".join(sorted(nums))


print(make_easier())
