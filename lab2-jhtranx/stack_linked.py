class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        return False

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if not (self.num_items == self.capacity):
            self.num_items += 1 #adds to number of items
            newNode = Node(item) #makes a new Node with item
            newNode.next = self.head #links new node with old head
            self.head = newNode #sets new Node to head
        else:
            raise IndexError

    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if not (self.num_items == 0):
            self.num_items -= 1
            returnItem = self.head.data
            self.head = self.head.next
            return returnItem
        else:
            raise IndexError

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if not (self.num_items == 0):
            return self.head.data
        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items

 