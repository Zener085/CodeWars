"""https://www.codewars.com/kata/5426d7a2c2c7784365000783 4 kyu"""

result: list[str]


def generate_parenthesis(s: str, n: int, o: int, c: int) -> None:
    global result
    if o == n == c:
        result.append(s)
        return

    if o < n:
        generate_parenthesis(s + "(", n, o + 1, c)

    if c < o:
        generate_parenthesis(s + ")", n, o, c + 1)


def balanced_parens(n: int) -> list[str]:
    global result
    result = []
    generate_parenthesis("", n, 0, 0)
    return result


print(balanced_parens(4))
