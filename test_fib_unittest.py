import unittest

from fib import fibonacci_iterative


class TestFib(unittest.TestCase):

    def test_fib_9_is_34(self):
        self.assertEqual(fibonacci_iterative(9), 34)

    def test_fib_negative_raise_error(self):
        expected = 34
        result = fibonacci_iterative(9)
        self.assertEqual(expected, result)

    def test_split(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)


if __name__ == '__main__':
    unittest.main()
