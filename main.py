import unittest


def monotone(arr):
    if not arr:
        return False

    direction = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i - 1]
            continue
        if (direction > 0 and arr[i] < arr[i - 1]) or (direction < 0 and arr[i] > arr[i - 1]):
            return False
    return True

class Test(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(monotone([]), False)
    def test_monotone_array(self):
        self.assertEqual(monotone([1, 12, 33, 54, 55]), True)
    def test_reverse_monotone_array(self):
        self.assertEqual(monotone([53, 41, 30, 2, 1]), True)
    def test_repeat_monotone_array(self):
        self.assertEqual(monotone([41, 41, 41, 41, 32, 2, 1]), True)
    def test_not_monotone_array(self):
        self.assertEqual(monotone([1, 2, 33, 4, 35, 24]), False)
    def test_not_monotone_reverse_array(self):
        self.assertEqual(monotone([5, 3, 2, 1, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()
