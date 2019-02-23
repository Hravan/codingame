import unittest

from temperatures import *

class TestClosestZero(unittest.TestCase):

    def test_no_temperature(self):
        nums = []
        n = 0
        self.assertEqual(closestZero(nums, n), 0)

    def test_one_temp(self):
        nums = [1]
        n = 1
        self.assertEqual(closestZero(nums, n), 1)

    def test_only_positive(self):
        nums = [2, 1, 5, 4]
        n = 4
        self.assertEqual(closestZero(nums, n), 1)

    def test_only_negative(self):
        nums = [-2, -5, -3, -4, -8]
        n = 5
        self.assertEqual(closestZero(nums, n), -2)

    def test_mixed(self):
        nums = [-2, -5, 3, 1, 2, -8]
        n = 6
        self.assertEqual(closestZero(nums, n), 1)

    def test_tie(self):
        nums = [-5, -2, 3, 2, 4]
        n = 5
        self.assertEqual(closestZero(nums, n), 2)

class TestCloserZero(unittest.TestCase):

    def test_not_tie(self):
        n = 1
        m = -2
        self.assertEqual(closerZero(n, m), 1)

    def test_the_same_numbers(self):
        n = 2
        m = 2
        self.assertEqual(closerZero(n, m), 2)

    def test_tie_opposite_numbers(self):
        n = 3
        m = -3
        self.assertEqual(closerZero(n, m), 3)


if __name__ == '__main__':
    unittest.main()
