import unittest
from queue_at_the_school import change_queue


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(change_queue("BGGBG", 1), "GBGGB")

    def test2(self):
        self.assertEqual(change_queue("BGGBG", 2), "GGBGB")

    def test3(self):
        self.assertEqual(change_queue("GGGB", 1), "GGGB")


if __name__ == '__main__':
    unittest.main()
