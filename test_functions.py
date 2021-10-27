import unittest
import functions


class TestMathTestCase(unittest.TestCase):

    def test_add(self) -> None:
        self.assertEqual(3, functions.add(1, 2))

    def test_sub(self) -> None:
        self.assertEqual(3, functions.sub(4, 1))

    def test_multiply(self) -> None:
        self.assertEqual(6, functions.multiply(2, 3))

    def test_divide(self) -> None:
        self.assertEqual(5, functions.divide(10, 2))

    def test_power(self) -> None:
        self.assertEqual(4, functions.power(2, 2))

    def test_add_float(self) -> None:
        self.assertEqual(4.0, functions.add(2.0, 2.0))


class TestStringTestCase(unittest.TestCase):

    def test_combined(self) -> None:
        self.assertEqual("hello world", functions.combine("hello", " world"))
