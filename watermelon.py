"""https://codeforces.com/problemset/problem/4/A  800"""


def is_divided(w: int) -> bool:
    return w != 2 and not w % 2


print("YES" if is_divided(int(input())) else "NO")
