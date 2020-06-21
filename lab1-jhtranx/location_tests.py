# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        loc1 = Location('SLO', 35.3, -120.7)
        loc2 = Location('SLO', 35.3, -120.7)
        self.assertTrue(loc1 == loc2)

    def test_init(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertTrue(loc.name == 'SLO')
        self.assertTrue(loc.lat == 35.3)
        self.assertTrue(loc.lon == -120.7)

    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
