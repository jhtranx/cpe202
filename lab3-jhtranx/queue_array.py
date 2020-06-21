
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.front = 0
        self.back = 0


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
            if not (self.num_items == 0): #queue is not empty

                if (self.back + 1) == self.capacity: #if at end of the queue array
                    self.items[0] = item 
                    self.num_items += 1
                    self.back = 0
                
                else: #if not at the end of queue array
                    self.items[self.back + 1] = item 
                    self.num_items += 1
                    self.back += 1

            else: #queue is empty
                self.items[self.back] = item 
                self.num_items += 1
            
        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if not (self.num_items == 0):
            if self.front == self.back:
                returnItem = self.items[self.front]
                self.num_items -= 1
                return returnItem

            elif (self.front + 1) == self.capacity: #if at end of the queue array
                returnItem = self.items[self.front]
                self.num_items -= 1
                self.front = 0
                return returnItem

            else: #if not at the end of queue array
                returnItem = self.items[self.front]
                self.num_items -= 1
                self.front += 1
                return returnItem
        else:
            raise IndexError


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

