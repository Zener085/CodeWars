"""https://codeforces.com/problemset/problem/266/B 800"""


def change_queue(queue: str, t: int) -> str:
    """Change 't' times queue - each time 1 boy skips 1 girl"""
    for i in range(t):
        queue = queue.replace("BG", "GB")

    return queue


# Time complexity - O(n^2), may be increased
if __name__ == "__main__":
    time = list(map(int, input().split()))[1]
    print(change_queue(input(), time))
