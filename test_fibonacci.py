import unittest
from fibonacci import calculate_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(calculate_fibonacci(0), 0)
        self.assertEqual(calculate_fibonacci(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(calculate_fibonacci(2), 1)
        self.assertEqual(calculate_fibonacci(3), 2)
        self.assertEqual(calculate_fibonacci(4), 3)
        self.assertEqual(calculate_fibonacci(10), 55)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_fibonacci(-1)
        with self.assertRaises(ValueError):
            calculate_fibonacci(-5)

if __name__ == '__main__':
    unittest.main()
