import unittest

from episode1 import *

class TestJump(unittest.TestCase):

    def test_row(self):
        w = 6
        h = 1
        jump = jump_device(w, h)
        drt = 'L'
        curr_bat = (5, 0)
        self.assertEqual(jump(drt, curr_bat), (2, 0))

    def test_column(self):
        w = 1
        h = 7
        jump = jump_device(w, h)
        drt = 'U'
        curr_bat = (0, 5)
        self.assertEqual(jump(drt, curr_bat), (0, 2))

    def test_U(self):
        w = 5
        h = 4
        jump = jump_device(w, h)
        drt = 'U'
        curr_bat = (1, 3)
        self.assertEqual(jump(drt, curr_bat), (1, 1))

    def test_UR(self):
        w = 5
        h = 4
        jump = jump_device(w, h)
        drt = 'UR'
        curr_bat = (1, 3)
        self.assertEqual(jump(drt, curr_bat), (3, 1))

    def test_R(self):
        w = 6
        h = 3
        jump = jump_device(w, h)
        drt = 'R'
        curr_bat = (1, 1)
        self.assertEqual(jump(drt, curr_bat), (3, 1))

    def test_DR(self):
        w = 6
        h = 7
        jump = jump_device(w, h)
        drt = 'DR'
        curr_bat = (2, 3)
        self.assertEqual(jump(drt, curr_bat), (4, 5))

    def test_D(self):
        w = 6
        h = 7
        jump = jump_device(w, h)
        drt = 'D'
        curr_bat = (2, 3)
        self.assertEqual(jump(drt, curr_bat), (2, 5))

    def test_DL(self):
        w = 6
        h = 7
        jump = jump_device(w, h)
        drt = 'DL'
        curr_bat = (2, 3)
        self.assertEqual(jump(drt, curr_bat), (0, 5))

    def test_L(self):
        w = 10
        h = 4
        jump = jump_device(w, h)
        drt = 'L'
        curr_bat = (8, 1)
        self.assertEqual(jump(drt, curr_bat), (3, 1))

    def test_UL(self):
        w = 6
        h = 7
        jump = jump_device(w, h)
        drt = 'UL'
        curr_bat = (4, 4)
        self.assertEqual(jump(drt, curr_bat), (1, 1))


if __name__ == '__main__':
    unittest.main()
