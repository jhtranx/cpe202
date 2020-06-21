# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self):
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)
        tlist = [2, 3, 1]
        self.assertEqual(max_list_iter(tlist), 3)
        tlist = [3, 1, 2]
        self.assertEqual(max_list_iter(tlist), 3)
        tlist = [1, 1, 1]
        self.assertEqual(max_list_iter(tlist), 1)
        tlist = [2, 1, 1]
        self.assertEqual(max_list_iter(tlist), 2)
        tlist = [1, 2, 1]
        self.assertEqual(max_list_iter(tlist), 2)
        tlist = [1, 1, 2]
        self.assertEqual(max_list_iter(tlist), 2)
        tlist = [1, 2, 2]
        self.assertEqual(max_list_iter(tlist), 2)
        tlist = [2, 2, 1]
        self.assertEqual(max_list_iter(tlist), 2)
        tlist = [2, 1, 2]
        self.assertEqual(max_list_iter(tlist), 2)
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_01(self):
        intlist = [1, 2, 3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3])
        intlist = [1, 2, 1]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [1, 2, 1])
        self.assertEqual(intlist, [1, 2, 1])
        intlist = [2, 2, 2]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [2, 2, 2])
        self.assertEqual(intlist, [2, 2, 2])
    
    def test_reverse_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list(tlist)

    def test_reverse_mutate(self):
        intlist = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])
        intlist = [1, 3, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 3, 1])
        intlist = [3, 3, 1]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [1, 3, 3])
        intlist = [3, 3, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 3, 3])
        intlist = [1, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 1])
        tlist = []
        self.assertEqual(reverse_list_mutate(tlist), None)

    def test_reverse_mutate_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(tlist)

    def test_reverse_rec(self):
        intlist = [1, 2, 3]
        self.assertEqual(reverse_rec(intlist),[3, 2, 1])
        self.assertEqual(intlist,[1, 2, 3])
        intlist = [1, 1, 1]
        self.assertEqual(reverse_rec(intlist),[1, 1, 1])
        self.assertEqual(intlist,[1, 1, 1])
        intlist = [2, 3, 1]
        self.assertEqual(reverse_rec(intlist),[1, 3, 2])
        self.assertEqual(intlist,[2, 3, 1])
        intlist = [1, 2, 2]
        self.assertEqual(reverse_rec(intlist),[2, 2, 1])
        self.assertEqual(intlist,[1, 2, 2])
        intlist = [2, 2, 1]
        self.assertEqual(reverse_rec(intlist),[1, 2, 2])
        self.assertEqual(intlist,[2, 2, 1])

    def test_reverse_rec_02(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)



if __name__ == "__main__":
        unittest.main()