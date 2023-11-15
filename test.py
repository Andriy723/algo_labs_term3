import unittest

from algo_labs_term3.main import min_size_board


class Test(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(min_size_board(10, 2, 3), 9)

    def test_equal_2(self):
        self.assertEqual(min_size_board(2, 1000000000, 999999999), (-1, -1))

    def test_equal_3(self):
        self.assertEqual(min_size_board(4, 1, 1), 2)
