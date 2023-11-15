import unittest

from src.main import greedy_algorithm, write_to_file, read_input


class TestCycleDetection(unittest.TestCase):
    def test_algorithm(self):
        num_employees, beer = 6, 3
        beer_preferences = "YNN YNY YNY NYY NYY NYN"
        result = greedy_algorithm(num_employees, beer, beer_preferences)
        self.assertEqual(result, 2)

    def test_algorithm_negative(self):
        num_employees, beer = 2, -2
        beer_preferences = "YN NY"
        result = greedy_algorithm(num_employees, beer, beer_preferences)
        self.assertFalse(result)

    def test_read_write(self):
        employees_num, beer_for_party, likes = read_input("input_txt")
        write_to_file(
            "output_txt", greedy_algorithm(employees_num, beer_for_party, likes)
        )

        with open("output_txt", "r") as output_file:
            data = int(output_file.read())

        with open("input_txt", "r") as input_file:
            data1 = str(input_file.read())

        self.assertEqual(data1, "6 3\nYNN YNY YNY NYY NYY NYN")
        self.assertEqual(data, 2)
