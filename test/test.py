import unittest
from src.kmp_search import kmp_search


class TestKMP(unittest.TestCase):
    def test_many_indexes(self):
        haystack_ = "AABABBABABABABDF"
        needle_ = "ABA"
        self.assertEqual(kmp_search(needle_, haystack_), [1, 6, 8, 10])

    def test_one_index(self):
        haystack_ = "AABABBABABABABDF"
        needle_ = "DF"
        self.assertEqual(kmp_search(needle_, haystack_), [14])

    def test_no_index(self):
        haystack_ = "AABABBABABABABDF"
        needle_ = "ABABDD"
        self.assertEqual(kmp_search(needle_, haystack_), [])
