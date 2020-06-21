import unittest
from bears import *

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    def test_bear_01_Given(self):
        self.assertTrue(bears(250))
        self.assertTrue(bears(42))
        self.assertFalse(bears(53))
        self.assertFalse(bears(41))

    def test_bear_02_Added(self):
        self.assertFalse(bears(7))
        self.assertFalse(bears(13))
        self.assertTrue(bears(84))
        self.assertFalse(bears(126))
        self.assertTrue(bears(168))
        self.assertTrue(bears(1260))
        self.assertTrue(bears(420))
        self.assertTrue(bears(2520))

if __name__ == "__main__":
    unittest.main()
