"""https://codeforces.com/problemset/problem/158/A 800"""


def accepted_players(n: int, k: int) -> int:
    scores = list(map(int, input().split()))
    res = 0
    for score in scores:
        if score == 0 or score < scores[k-1]:
            break
        res += 1

    return res


print(accepted_players(*list(map(int, input().split()))))
