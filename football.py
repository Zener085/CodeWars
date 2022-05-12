"""https://codeforces.com/problemset/problem/96/A 900"""


def is_dangerous(case: str) -> bool:
    return case.find("1" * 7) != -1 or case.find("0" * 7) != -1


print("YES" if is_dangerous(input()) else "NO")
