import unittest
from Math import add, multiply

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(2, 3, 4), 24)
        self.assertEqual(multiply(1, 2, 3, 4, 5), 120)
        self.assertEqual(multiply(), 1)  # Empty input should return 1
        self.assertEqual(multiply(5), 5)  # Single input should return itself

if __name__ == '__main__':
    unittest.main()