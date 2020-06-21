
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = None
        self.back = None
        self.num_items = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if not (self.num_items == self.capacity):
            if self.num_items == 0:
                self.num_items += 1 #adds to number of items
                newNode = Node(item) #makes a new Node with item
                self.front = newNode
                self.back = newNode
            else:
                self.num_items += 1 #adds to number of items
                newNode = Node(item) #makes a new Node with item
                self.back.next = newNode #sets oldback next to new node
                self.back = newNode #sets back to new node
        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if not (self.num_items == 0):
            self.num_items -= 1
            returnItem = self.front.item
            self.front = self.front.next
            return returnItem
        else:
            raise IndexError


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
