"""https://codeforces.com/problemset/problem/71/A 800"""


def long_words(n: int) -> list[str]:
    words = []
    for i in range(n):
        word = input()
        length = len(word)
        if length <= 10:
            words.append(word)
        else:
            words.append(word[0] + str(length-2) + word[-1])

    return words


print(*long_words(int(input())), sep="\n")
