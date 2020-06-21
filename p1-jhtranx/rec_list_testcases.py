import unittest
from  rec_list import *

# Starter test cases - write more!

class TestRecList(unittest.TestCase):

    def test_first1(self):
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"49ers")
        strlist = Node("xyz", Node("49ers", Node("Abc", None)))
        self.assertEqual(first_string(strlist),"49ers")
        strlist = Node("49ers", Node("xyz", Node("Abc", None)))
        self.assertEqual(first_string(strlist),"49ers")

        strlist = Node("xyz", Node("xyz", Node("xyz", None)))
        self.assertEqual(first_string(strlist),"xyz")
        strlist = Node("xyz", Node("xyz", Node("abc", None)))
        self.assertEqual(first_string(strlist),"abc")

        strlist = None
        self.assertEqual(first_string(strlist), None)

        strlist = Node("xyz", None)
        self.assertEqual(first_string(strlist),"xyz")
    
    def test_first2(self):
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertNotEqual(first_string(strlist),"Abc")
        strlist = Node("xyz", Node("49ers", Node("Abc", None)))
        self.assertNotEqual(first_string(strlist),"xyz")
        strlist = Node("49ers", Node("xyz", Node("Abc", None)))
        self.assertNotEqual(first_string(strlist),"Abc")

    def test_split1(self):
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))
        strlist = Node("xyz", Node("49ers", Node("Abc", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))
        strlist = Node("49ers", Node("xyz", Node("Abc", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))

        strlist = Node("49ers", Node("Abc", Node("Abc", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', Node('Abc', None)), None, Node('49ers', None)))
        
        #one of each
        strlist = Node("49ers", Node("xyz", None))
        self.assertEqual(split_list(strlist),(None, Node('xyz', None), Node('49ers', None)))
        strlist = Node("49ers", None)
        self.assertEqual(split_list(strlist),(None, None, Node('49ers', None)))
        strlist = Node("xyz", None)
        self.assertEqual(split_list(strlist),(None, Node('xyz', None), None))
        strlist = Node("abc", None)
        self.assertEqual(split_list(strlist),(Node('abc', None), None, None))

        #simple
        strlist = Node("49ers", Node("xyz", None))
        self.assertNotEqual(split_list(strlist),(None, None, Node('49ers', Node('xyz', None))))
        strlist = Node("49ers", None)
        self.assertNotEqual(split_list(strlist),(None, Node('49ers', None), None))

        #all the same
        strlist = Node("aaa", Node("aaa", Node("aaa", None)))
        self.assertEqual(split_list(strlist),(Node('aaa', Node('aaa', Node('aaa', None))), None, None))
        strlist = Node("bbb", Node("bbb", Node("bbb", None)))
        self.assertEqual(split_list(strlist),(None, Node('bbb', Node('bbb', Node('bbb', None))), None))
        strlist = Node("$", Node("$", Node("$", None)))
        self.assertEqual(split_list(strlist),(None, None, Node('$', Node('$', Node('$', None)))))

    def test_split_None(self):
        strlist = None
        self.assertEqual(split_list(strlist), (None, None, None))

    def test_split2(self):
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist),(Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))

    def test_repr(self):
        self.assertEqual(repr(Node(None, None)), "Node(None, None)")
    

if __name__ == "__main__":
        unittest.main()