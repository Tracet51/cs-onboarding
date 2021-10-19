import unittest
import mather


class TestMathTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, mather.add(1, 2))

    def test_sub(self):
        self.assertEqual(3, mather.sub(2, 4))
