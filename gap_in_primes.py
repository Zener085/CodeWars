"""https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4 5 kyu"""

from math import sqrt


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def gap(g: int, m: int, n: int):
    while m + g <= n:
        if is_prime(m) and is_prime(m + g) and not max(is_prime(i) for i in range(m+1, m+g)):
            return [m, m+g]
        m += 1

    return None
