class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        dummyNode = Node("dummy")
        dummyNode.next = dummyNode
        dummyNode.prev = dummyNode
        self.head = dummyNode


    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        #if the dummy node refers to itself, the list is empty
        if self.head.next == self.head:
            return True


    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''

        currentNode = self.head.next
        n = Node(item)
        while currentNode != self.head:
            if item < currentNode.item:
                break
            if item == currentNode.item:
                return False
            else:
                currentNode = currentNode.next

        #code for linking
        n.next = currentNode
        n.prev = currentNode.prev
        n.prev.next = n
        currentNode.prev = n
        return True


    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        
        currentNode = self.head.next

        while currentNode != self.head:
            if currentNode.item == item:
                #unlinking the node from the list
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                return True
            else:
                currentNode = currentNode.next
        return False

        
    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''

        currentNode = self.head.next
        index = 0

        while currentNode != self.head:
            if currentNode.item == item:
                return index
            else:
                currentNode = currentNode.next
                index += 1
        return None


    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''

        currentNode = self.head.next
        indexIN = 0

        if index < 0:
            raise IndexError

        while currentNode != self.head:
            if index == indexIN:
                popItem = currentNode.item
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                return popItem
            else:
                currentNode = currentNode.next
                indexIN += 1
        raise IndexError


    def search_helper(self, node, item):
        if node is self.head:
            return False
        if node.item == item:
            return True
        return self.search_helper(node.next, item)

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return (self.search_helper(self.head.next, item))


    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        
        currentNode = self.head.next
        pythonlist = []

        while currentNode != self.head:
            pythonlist.append(currentNode.item)
            currentNode = currentNode.next
        return pythonlist


    def python_list_reversed_helper(self, pythonlist, node):
        if node is self.head:
            return pythonlist
        pythonlist.append(node.item)
        return self.python_list_reversed_helper(pythonlist, node.prev)

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''

        currentNode = self.head.prev
        pythonlist = []
        return (self.python_list_reversed_helper(pythonlist, currentNode))


    def size_helper(self, node):
        if node is self.head:
            return 0
        return 1 + self.size_helper(node.next)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return (self.size_helper(self.head.next))

    