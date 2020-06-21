import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

        nums = [5, 4, 3, 6, 2, 1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 15)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

        nums = [10, 47, 5, 12, 26]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [5, 10, 12, 26, 47])

        #empty list case
        nums = []
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])


    def test_simple_1(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

        nums = [5, 4, 3, 6, 2, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 13)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6])

        nums = [10, 47, 5, 12, 26]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 7)
        self.assertEqual(nums, [5, 10, 12, 26, 47])

        #empty list case
        nums = []
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

if __name__ == '__main__': 
    unittest.main()
