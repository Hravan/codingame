import unittest

from horse_racing_duals import *

class TestFindDual(unittest.TestCase):

    def test_draw(self):
        horses = [3, 5, 8, 9, 9]
        self.assertEqual(find_dual(horses), 0)

    def test_simple_case(self):
        horses = [3, 5, 8, 9]
        self.assertEqual(find_dual(horses), 1)

    def test_any_order(self):
        horses = [10, 5, 15, 17, 3, 8, 11, 28, 6, 55, 7]
        self.assertEqual(find_dual(horses), 1)

if __name__ == '__main__':
    unittest.main()
