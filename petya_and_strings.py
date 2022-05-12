"""https://codeforces.com/problemset/problem/112/A 800"""


def compare_strings() -> int:
    first = input().lower()
    second = input().lower()

    for i in range(len(first)):
        if ord(first[i]) < ord(second[i]):
            return -1
        if ord(first[i]) > ord(second[i]):
            return 1

    return 0


print(compare_strings())
