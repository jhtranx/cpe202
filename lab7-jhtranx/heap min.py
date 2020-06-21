
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.capacity = capacity
        self.heapList = [0]
        self.size = 0


    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        #check if the heap is full
        if self.size < self.capacity: #if heap is not full
            self.heapList.append(item) #append to end of list
            self.size += 1 #increase size by 1
            index = self.size
            # print(self.heapList) #PRINT DEBUG
            self.perc_up(index)
            print(self.heapList)
            return True

        elif self.size == self.capacity: #if heap is full
            return False
        

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.size == 0:
            return None
        return self.heapList[1]


    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # if self.is_empty():
        #     return None
        # maxReturn = self.heapList[1] #return the max
        # temp = self.heapList.pop() #delete last element
        # self.heapList[1] = temp #move last element to front
        # self.perc_down(1)
        # self.size -= 1
        # return maxReturn
        if self.is_empty():
            return None

        elif self.size == 1:
            returnItem = self.heapList[1]
            self.size = 0
            self.heapList = [0]
            return returnItem
        
        maxReturn = self.heapList[1] #return the max

        temp = self.heapList[self.size] #create temp value of last element
        self.heapList[1] = temp #move last element to front
        self.heapList.pop() #delete last element
        
        self.size -= 1
        self.perc_down(1)
        return maxReturn


    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heapList[1:]
            

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        #check capacity
        if len(alist) > self.capacity:
            self.capacity = len(alist)

        #discards all items from heap
        self.heapList = [0]
        self.size = 0
        #insert items into the array start at spot 1 (no order)
        for i in range(len(alist)):
            self.heapList.append(alist[i])
            self.size += 1
        
        parentIndex = self.size // 2 #to find last parent size // 2
        #from last parent to root
        while parentIndex > 0:
            # print(self.heapList) #PRINT DEBUG
            self.perc_down(parentIndex) #perc down each element
            parentIndex = parentIndex - 1 
            

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        if self.size == 0:
            return True
        return False


    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        if self.size < self.capacity:
            return False
        return True
   
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity
    
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size

        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        #prepwork
        lastElement = self.heapList[i] #create a temp value for last leaf element
        currentIndex = i
        childIndex1 = currentIndex * 2
        childIndex2 = currentIndex * 2 + 1
        
        #while there is a left child to the current index
        while childIndex1 <= self.size:
            #if the right child to current index does not exist
            if childIndex2 > self.size:
                #set element
                childElement1 = self.heapList[childIndex1]

                if (lastElement <= childElement1):
                    self.heapList[currentIndex] = lastElement #set current index to last element
                    return
                else:
                    #shift child to current index
                    self.heapList[currentIndex] = childElement1
                    
                    #set new indexes
                    currentIndex = childIndex1
                    childIndex1 = currentIndex * 2
                    childIndex2 = currentIndex * 2 + 1
            
            #if the right child to current index does exist
            else:
                #set elements
                childElement1 = self.heapList[childIndex1]
                childElement2 = self.heapList[childIndex2]

                #if last element is less than equal to BOTH of its children
                if (lastElement <= childElement1) and (lastElement <= childElement2):
                    self.heapList[currentIndex] = lastElement #set current index to last element
                    return

                #if last element is greater than one or both of its children
                else:
                    #find smallest child and its index
                    childSmall = min(childElement1, childElement2)
                    if childSmall == childElement1:
                        childSmallIndex = childIndex1
                    else:
                        childSmallIndex = childIndex2

                    #shift smallest child to current index
                    self.heapList[currentIndex] = childSmall
                    
                    #set new indexes
                    currentIndex = childSmallIndex
                    childIndex1 = currentIndex * 2
                    childIndex2 = currentIndex * 2 + 1
        self.heapList[currentIndex] = lastElement #set current index to last element
        return

        
    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        #prepwork
        startItem = self.heapList[i]
        currentIndex = i
        parentIndex = currentIndex // 2
        # print(parentIndex)
        parentItem = self.heapList[parentIndex]
        # print(parentItem)

        #while start item is less than or equal to parent item
        while (startItem <= parentItem) and (parentIndex != 0):
            self.heapList[currentIndex] = parentItem #shift parent item to current item index
            currentIndex = parentIndex #set current index to parent index
            parentIndex = currentIndex // 2 #set new parent index
            parentItem = self.heapList[parentIndex] #set new parent item
            
        #if it is greater than or done with iteration
        self.heapList[currentIndex] = startItem #replace current item with start item


    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''

minheap = MaxHeap()
minheap.enqueue(10)
minheap.enqueue(12)
minheap.enqueue(1)
minheap.enqueue(14)
minheap.enqueue(6)
minheap.enqueue(5)
minheap.enqueue(8)
minheap.enqueue(15)
minheap.enqueue(3)
minheap.enqueue(9)
minheap.enqueue(7)
minheap.enqueue(4)
minheap.enqueue(11)
minheap.enqueue(13)
minheap.enqueue(2)
minheap.dequeue()
print(minheap.heapList)
minheap.dequeue()
print(minheap.heapList)
minheap.dequeue()
print(minheap.heapList)