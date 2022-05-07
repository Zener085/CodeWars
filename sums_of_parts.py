"""https://www.codewars.com/kata/5ce399e0047a45001c853c2b 6 kyu"""


def parts_sums(ls: list) -> list:
    ps = [sum(ls)]

    for i in ls:
        ps.append(ps[-1] - i)

    return ps
