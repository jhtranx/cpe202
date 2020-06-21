import unittest
from queue_array import Queue
# from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
    
    def test_simple(self):
        queue = Queue(5)
        queue.enqueue(0)
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.size(),1)

        queue = Queue(3)
        queue.enqueue('lets get started')
        queue.enqueue('yo this kinda fun')
        queue.enqueue('i know bro')
        self.assertEqual(queue.size(), 3)
        with self.assertRaises(IndexError):  # used to check for exception
            queue.enqueue('drain gang')
        self.assertEqual(queue.size(), 3)
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.dequeue(),'lets get started')
        self.assertEqual(queue.dequeue(),'yo this kinda fun')
        queue.enqueue('more stuff')
        queue.dequeue()
        queue.dequeue()
        with self.assertRaises(IndexError):  # used to check for exception
            queue.dequeue()
        self.assertFalse(queue.is_full())

    def test_isempty(self):
        queue = Queue(3)
        self.assertTrue(queue.is_empty())
        queue = Queue(3)
        queue.enqueue('bananamilk')
        self.assertFalse(queue.is_empty())

    def test_isfull(self):
        queue = Queue(3)
        queue.enqueue('I am not full')
        queue.enqueue('I am kinda hungry')
        self.assertFalse(queue.is_full())
        queue = Queue(3)
        queue.enqueue('I am full')
        queue.enqueue('I am so full')
        queue.enqueue('I am really full')
        self.assertTrue(queue.is_full())

    def test_enqueue(self):
        queue = Queue(3)
        queue.enqueue('drain gang')
        queue.enqueue('drain gang')
        queue.enqueue('drain gang')
        with self.assertRaises(IndexError):  # used to check for exception
            queue.enqueue('drain gang')

    def test_dequeue(self):
        queue = Queue(3)
        queue.enqueue('im first!')
        queue.enqueue('im second')
        queue.enqueue('this sucks')
        self.assertEqual(queue.dequeue(),'im first!')

        queue = Queue(3)
        with self.assertRaises(IndexError):  # used to check for exception
            queue.dequeue()

    def test_size(self):
        queue = Queue(3)
        queue.enqueue('drain')
        queue.enqueue('drained')
        queue.enqueue('drain gang')
        self.assertEqual(queue.size(), 3)

        queue = Queue(3)
        self.assertEqual(queue.size(), 0)

if __name__ == '__main__': 
    unittest.main()
