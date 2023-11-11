import unittest
from episode1 import *

class TestFindNeighbours(unittest.TestCase):

    def test_one_node(self):
        grid = '0'
        fn = find_neighbours(1, 1, grid)
        self.assertEqual(next(fn), '0 0 -1 -1 -1 -1')

    def test_one_row(self):
        grid = ['0.00.']
        fn = find_neighbours(5, 1, grid)
        self.assertEqual(next(fn), '0 0 2 0 -1 -1')
        self.assertEqual(next(fn), '2 0 3 0 -1 -1')
        self.assertEqual(next(fn), '3 0 -1 -1 -1 -1')

    def test_one_column(self):
        grid = ['0',
                '.',
                '.',
                '0',
                '.']
        fn = find_neighbours(1, 5, grid)
        self.assertEqual(next(fn), '0 0 -1 -1 0 3')
        self.assertEqual(next(fn), '0 3 -1 -1 -1 -1')

    def test_2d_grid(self):
        grid = ['0.0.',
                '..00',
                '00.0']
        fn = find_neighbours(4, 3, grid)
        self.assertEqual(next(fn), '0 0 2 0 0 2')
        self.assertEqual(next(fn), '2 0 -1 -1 2 1')
        self.assertEqual(next(fn), '2 1 3 1 -1 -1')
        self.assertEqual(next(fn), '3 1 -1 -1 3 2')

if __name__ == '__main__':
    unittest.main()
