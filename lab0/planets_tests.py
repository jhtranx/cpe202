import unittest
from planets import *

class TestCases(unittest.TestCase):

    def test_mars_1(self):
        self.assertEqual(find_mars(136), 51.68)

    def test_mars_2(self):
        self.assertEqual(find_mars(200), 76.00)

    def test_mars_3(self):
        self.assertEqual(find_mars(52), 19.76)


    def test_jupiter_1(self):
        self.assertEqual(find_jupiter(136), 318.24)

    def test_jupiter_2(self):
        self.assertNotEqual(find_jupiter(52), 19.76)

    def test_jupiter_3(self):
        self.assertEqual(find_jupiter(200), 468)

if __name__ == '__main__':
    unittest.main()