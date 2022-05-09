"""https://www.codewars.com/kata/5765870e190b1472ec0022a2 4 kyu"""

from collections import deque


def path_finder(maze: str) -> bool:
    maze = list(map(list, maze.split("\n")))
    size = len(maze)
    queue = deque()
    queue.append([0, 0])

    while queue:
        element = queue.pop()
        if element == [size-1, size-1]:
            return True

        x, y = element[0], element[1]

        if maze[x][y] == 'W':
            continue

        if size > x and size > y + 1 and maze[x][y+1] == '.':
            queue.appendleft([x, y+1])

        if size > x+1 and size > x and maze[x+1][y] == '.':
            queue.appendleft([x+1, y])

        if x >= 0 and y-1 >= 0 and maze[x][y-1] == '.':
            queue.appendleft([x, y-1])

        if x-1 >= 0 and y >= 0 and maze[x-1][y] == '.':
            queue.appendleft([x-1, y])

        maze[x][y] = 'W'

    return False
