def bubble_sort(array: list) -> list:
    """return list sorted by bubble sort"""
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":  # for example
    example_list = list(map(int, input().split()))
    example_list = bubble_sort(example_list)
    print(*example_list)
