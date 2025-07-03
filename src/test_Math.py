import unittest
from Math import add, add_stream

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 2, 3), 6)
        self.assertEqual(add(1, 2, 3, 4, 5), 15)
        self.assertEqual(add(), 0)

    def test_add_stream(self):
        self.assertEqual(add_stream([1, 2, 3]), 6)
        self.assertEqual(add_stream(range(1, 6)), 15)
        self.assertEqual(add_stream([]), 0)
        self.assertEqual(add_stream(iter([1, 2, 3, 4, 5])), 15)

if __name__ == '__main__':
    unittest.main()