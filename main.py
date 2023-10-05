import unittest


def min_size_board(leaf_num, width, height):
    if leaf_num not in range(1, 1012):
        return -1, -1

    if width not in range(1, 109):
        return -1, -1

    if height not in range(1, 109):
        return -1, -1

    left = max(width, height)
    right = left * leaf_num
    while left < right:
        mid = (left + right) // 2
        if (mid // width) * (mid // height) >= leaf_num:
            right = mid
        else:
            left = mid + 1
    return left


class Test(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(min_size_board(10, 2, 3), 9)

    def test_equal_2(self):
        self.assertEqual(min_size_board(2, 1000000000, 999999999), (-1, -1))

    def test_equal_3(self):
        self.assertEqual(min_size_board(4, 1, 1), 2)
