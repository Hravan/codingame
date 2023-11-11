import unittest
import math

from episode1 import *

class TestDirection(unittest.TestCase):

    def test_direction_north(self):
        p1 = (2, 3)
        p2 = (2, 2)
        self.assertEqual(direction(p1, p2), 'N')

    def test_direction_south(self):
        p1 = (3, 0)
        p2 = (2, 3)
        self.assertEqual(direction(p1, p2), 'S')

    def test_direction_east(self):
        p1 = (0, 1)
        p2 = (3, 0)
        self.assertEqual(direction(p1, p2), 'E')

    def test_direction_west(self):
        p1 = (3, 0)
        p2 = (0, 1)
        self.assertEqual(direction(p1, p2), 'W')

    def test_direction_north_east(self):
        p1 = (2, 2)
        p2 = (3, 1)
        self.assertEqual(direction(p1, p2), 'NE')

    def test_direction_north_west(self):
        p1 = (2, 1)
        p2 = (1, 0)
        self.assertEqual(direction(p1, p2), 'NW')

    def test_direction_south_east(self):
        p1 = (1, 1)
        p2 = (2, 2)
        self.assertEqual(direction(p1, p2), 'SE')

    def test_direction_south_west(self):
        p1 = (2, 0)
        p2 = (1, 1)
        self.assertEqual(direction(p1, p2), 'SW')

class TestFindAngle(unittest.TestCase):

    def test_findAngle_pi_over_four(self):
        p1 = (1, 1)
        p2 = (2, 0)
        self.assertEqual(findAngle(p1, p2), math.pi / 4)

        p3, p4 = p2, p1
        self.assertEqual(findAngle(p3, p4), - 3 * math.pi / 4)

    def test_findAngle_zero(self):
        p1 = (1, 1)
        p2 = (2, 1)
        self.assertEqual(findAngle(p1, p2), 0)

    def test_findAngle_pi(self):
        p1 = (2, 1)
        p2 = (1, 1)
        self.assertEqual(findAngle(p1, p2), math.pi)

    def test_findAngle_unusual(self):
        p1 = (0, 1)
        p2 = (3, 0)
        delta_x = p2[0] - p1[0]
        delta_y = -(p2[1] - p1[1])
        self.assertEqual(findAngle(p1, p2), math.atan(delta_y / delta_x))

class TestAngleToDirection(unittest.TestCase):

    def test_N(self):
        angle = math.pi / 2
        self.assertEqual(angleToDirection(angle), 'N')

    def test_S(self):
        angle = -math.pi / 2
        self.assertEqual(angleToDirection(angle), 'S')

    def test_E(self):
        angle = -math.pi / 16
        self.assertEqual(angleToDirection(angle), 'E')

    def test_W(self):
        angle = 7.5 * math.pi / 8
        self.assertEqual(angleToDirection(angle), 'W')

    def test_NE(self):
        angle = 3 / 16 * math.pi
        self.assertEqual(angleToDirection(angle), 'NE')

    def test_NW(self):
        angle = 11 / 16 * math.pi
        self.assertEqual(angleToDirection(angle), 'NW')

    def test_SE(self):
        angle = (-5) / 16 * math.pi
        self.assertEqual(angleToDirection(angle), 'SE')

    def test_SW(self):
        angle = (-11) / 16 * math.pi
        self.assertEqual(angleToDirection(angle), 'SW')

class TestMove(unittest.TestCase):

    def test_N(self):
        drtn = 'N'
        start = (1, 1)
        self.assertEqual(move(drtn, start), (1, 0))

    def test_S(self):
        drtn = 'S'
        start = (1, 0)
        self.assertEqual(move(drtn, start), (1, 1))

    def test_E(self):
        drtn = 'E'
        start = (1, 0)
        self.assertEqual(move(drtn, start), (2, 0))

    def test_W(self):
        drtn = 'W'
        start = (1, 0)
        self.assertEqual(move(drtn, start), (0, 0))

    def test_NE(self):
        drtn = 'NE'
        start = (1, 1)
        self.assertEqual(move(drtn, start), (2, 0))

    def test_NW(self):
        drtn = 'NW'
        start = (1, 1)
        self.assertEqual(move(drtn, start), (0, 0))

    def test_SE(self):
        drtn = 'SE'
        start = (1, 1)
        self.assertEqual(move(drtn, start), (2, 2))

    def test_SW(self):
        drtn = 'SW'
        start = (1, 1)
        self.assertEqual(move(drtn, start), (0, 2))





if __name__ == '__main__':
    unittest.main()
