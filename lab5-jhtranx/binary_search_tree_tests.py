import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])
        

    def test_is_empty(self):
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        self.assertFalse(bst.is_empty())


    def test_search(self):
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        bst.insert(20, 'yes')
        bst.insert(30, 'nar')
        self.assertFalse(bst.search(40))

        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        bst.insert(20, 'yes')
        bst.insert(30, 'nar')
        self.assertTrue(bst.search(30))

        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        bst.insert(5, 'coffee')
        bst.insert(20, 'yes')
        bst.insert(30, 'nar')
        self.assertTrue(bst.search(5))

    
    def test_find_min(self):
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        bst.insert(5, 'coffee')
        bst.insert(20, 'yes')
        bst.insert(30, 'nar')
        self.assertEqual(bst.find_min(), (5, 'coffee'))

    def test_find_max(self):
        bst = BinarySearchTree()
        bst.insert(10, 'stuff')
        bst.insert(5, 'coffee')
        bst.insert(20, 'yes')
        bst.insert(30, 'nar')
        self.assertEqual(bst.find_max(), (30, 'nar'))


    def test_inorder_traversal(self):
        bst = BinarySearchTree()
        bst.insert(5, 'drain')
        bst.insert(4, 'ecco')
        bst.insert(3, '2k')
        bst.insert(2, 'drained')
        bst.insert(1, 'out')
        bst.insert(6, 'peroxide')
        bst.insert(7, 'yes')
        self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 5, 6, 7])
    
    def test_preorder_traversal(self):
        bst = BinarySearchTree()
        bst.insert(5, 'drain')
        bst.insert(4, 'ecco')
        bst.insert(3, '2k')
        bst.insert(2, 'drained')
        bst.insert(1, 'out')
        bst.insert(6, 'peroxide')
        bst.insert(7, 'yes')
        self.assertEqual(bst.preorder_list(), [5, 4, 3, 2, 1, 6, 7])

        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(4)
        bst.insert(2)
        bst.insert(6)
        bst.insert(1)
        bst.insert(7)
        self.assertEqual(bst.preorder_list(), [5, 3, 2, 1, 4, 6, 7])

    def test_level_traversal(self):
        bst = BinarySearchTree()
        bst.insert("a")
        bst.insert("b")
        bst.insert("c")
        bst.insert("d")
        bst.insert("e")
        bst.insert("f")
        bst.insert("g")
        self.assertEqual(bst.level_order_list(), ["a", "b", "c", "d", "e", "f", "g"])

        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(4)
        bst.insert(2)
        bst.insert(6)
        bst.insert(1)
        bst.insert(7)
        self.assertEqual(bst.level_order_list(), [5, 3, 6, 2, 4, 7, 1])

    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(10))
        self.assertEqual(bst.find_max(), None)
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.tree_height(), None)
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])

if __name__ == '__main__': 
    unittest.main()
