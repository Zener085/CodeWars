"""https://codeforces.com/problemset/problem/133/A 900"""


def is_output(program: str) -> bool:
    for i in ['H', 'Q', '9']:
        if i in program:
            return True

    return False


print("YES" if is_output(input()) else "NO")
