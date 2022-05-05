"""https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/ 6 kyu"""


def duplicate_count(text: str) -> int:
    count = 0
    text = text.lower()
    while text != "":
        char = text[-1]
        count += char in text[:-1]
        text = text.replace(char, '')

    return count
