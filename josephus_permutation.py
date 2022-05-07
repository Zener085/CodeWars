"""https://www.codewars.com/kata/5550d638a99ddb113e0000a2 5 kyu"""


def josephus(items: list, k: int) -> list:
    index = 0
    result = []
    while len(items) != 0:
        index += k - 1
        index = index % len(items)
        result.append(items.pop(index))

    return result
