import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

        stack = Stack(3)
        stack.push(1)
        self.assertFalse(stack.is_empty())
        stack.pop()
        with self.assertRaises(IndexError):  # used to check for exception
            stack.peek()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        stack.push(3)
        with self.assertRaises(IndexError):  # used to check for exception
            stack.push(4)
        self.assertEqual(stack.size(), 3)
        self.assertFalse(stack.is_empty())
        stack.pop()
        stack.pop()
        stack.pop()
        with self.assertRaises(IndexError):  # used to check for exception
            stack.pop()
        with self.assertRaises(IndexError):  # used to check for exception
            stack.peek()
        
    def test_isempty(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())

        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_isfull(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertTrue(stack.is_full())

        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        self.assertFalse(stack.is_full())

    def test_push(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(IndexError):  # used to check for exception
            stack.push(3)

    def test_pop(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)

        stack = Stack(3)
        with self.assertRaises(IndexError):  # used to check for exception
            stack.pop()

    def test_peek(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)

        stack = Stack(3)
        with self.assertRaises(IndexError):  # used to check for exception
            stack.peek()

    def test_size(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)

        stack = Stack(3)
        self.assertEqual(stack.size(), 0)

        

if __name__ == '__main__': 
    unittest.main()
