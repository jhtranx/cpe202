import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)


    def test_stress(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.python_list(), [10, 20, 30])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.index(30), 2)
        with self.assertRaises(IndexError):  # used to check for exception
            t_list.pop(-1)
        self.assertTrue(t_list.search(20))
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.pop(0), 20)
        self.assertTrue(t_list.remove(30))
        self.assertTrue(t_list.is_empty())
        t_list.add(300)
        t_list.add(200)
        t_list.add(100)
        self.assertEqual(t_list.python_list_reversed(), [300, 200, 100])
        self.assertFalse(t_list.remove(10))


    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())

        t_list = OrderedList()
        t_list.add(10)
        self.assertFalse(t_list.is_empty())


    def test_add(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(2)
        t_list.add(3)
        t_list.add(1)
        t_list.add(4)
        self.assertEqual(t_list.head.next.item, 1)
        self.assertEqual(t_list.head.next.next.item, 2)
        self.assertEqual(t_list.head.next.next.next.item, 3)
        self.assertEqual(t_list.head.next.next.next.next.item, 4)
        self.assertEqual(t_list.head.next.next.next.next.next.item, 5)
        self.assertEqual(t_list.head.prev.item, 5)
        self.assertEqual(t_list.head.prev.prev.item, 4)
        self.assertEqual(t_list.head.prev.prev.prev.item, 3)
        self.assertEqual(t_list.head.prev.prev.prev.prev.item, 2)
        self.assertEqual(t_list.head.prev.prev.prev.prev.prev.item, 1)

        t_list = OrderedList()
        self.assertTrue(t_list.add(5))
        self.assertFalse(t_list.add(5))


    def test_remove(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.remove(10))


    def test_index(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(20), 1)
        self.assertEqual(t_list.index(30), 2)

        t_list = OrderedList()
        self.assertEqual(t_list.index(10), None)


    def test_pop(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        with self.assertRaises(IndexError):  # used to check for exception
            t_list.pop(0)
        
        t_list.add(10)
        t_list.add(20)
        self.assertEqual(t_list.pop(1), 20)

        with self.assertRaises(IndexError):  # used to check for exception
            t_list.pop(-1)


    def test_search(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertTrue(t_list.search(10))
        t_list.add(20)
        self.assertTrue(t_list.search(20))
        t_list.add(30)
        self.assertFalse(t_list.search(40))
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.search(10))
        self.assertTrue(t_list.search(20))


    def test_pythonlist(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.python_list(), [10, 20, 30])


    def test_pythonlist_reversed(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.python_list_reversed(), [30, 20, 10])

    
    def test_size(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.size(), 3)


if __name__ == '__main__': 
    unittest.main()
