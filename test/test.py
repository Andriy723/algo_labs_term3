import unittest

from algo_labs_term3.src.main import main


class TestCycleDetection(unittest.TestCase):
    def test_ordinary_num(self):
        result = main("input_txt", "output_txt")
        self.assertEqual(result, 2)

    def test_big_num(self):
        result = main("input1_txt", "output1_txt")
        self.assertEqual(result, 2)

    def test_nothing(self):
        result = main("input2_txt", "output2_txt")
        self.assertFalse(result)
