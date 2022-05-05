"""https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python 6 kyu"""


def bouncing_ball(h: int, bounce: int, window: int) -> int:
    if not h > 0 or not 0 < bounce < 1 or not window < h:
        return -1

    q = 1
    h *= bounce

    while h > window:
        h *= bounce
        q += 2

    return q
