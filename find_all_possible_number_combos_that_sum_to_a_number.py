"""https://www.codewars.com/kata/555b1890a75b930e63000023 4 kyu"""

result: list[list[int]]


def generate_sum(n: int, i: int, numbers: list[int]) -> None:
    global result

    numbers.append(i)

    if sum(numbers) == n:
        result.append(numbers)
        return

    if sum(numbers) > n:
        return

    for j in range(i, n):
        generate_sum(n, j, numbers.copy())


def combos(n):
    global result
    result = [[n]]

    for i in range(1, n // 2 + 1):
        generate_sum(n, i, [].copy())

    return result


print(combos(4))
