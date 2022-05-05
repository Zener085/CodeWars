"""https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python 4 kyu"""


class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def __increase_rank(self):
        """set new values for rank and progress if necessary"""
        while self.progress >= 100:
            self.rank += 1 + (self.rank == -1)
            self.progress -= 100
        if self.rank >= 8:
            self.rank, self.progress = 8, 0

    def inc_progress(self, rank: int) -> None:
        """increase progress of the user"""
        assert rank in list(range(-8, 0)) + list(range(1, 9))
        diff = rank - (rank > 0) - self.rank + (self.rank > 0)
        self.progress += (0, 1, 3, diff * diff * 10)[(diff > 0) + (diff >= 0) + (diff >= -1)]
        self.__increase_rank()
