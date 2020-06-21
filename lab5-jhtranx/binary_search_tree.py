from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None


    def is_empty(self): # returns True if tree is empty, else False
        if self.root == None:
            return True
        return False


    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.root == None:
            return False
        else:
            currentNode = self.root
            return self.search_helper(currentNode, key)
    
    def search_helper(self, node, key): #takes in a node and helps search
        #base cases - when you find the key return True, when you dont return False
        if node == None:
            return False
        if node.key == key:
            return True

        #traversal - when it is greater go left, when less go right
        if node.key > key:
            return self.search_helper(node.left, key)
        elif node.key < key:
            return self.search_helper(node.right, key)


    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        
        #create new node
        newNode = TreeNode(key, data)

        #if there is no root
        if self.root == None:
            self.root = newNode
        else:
            #if there is a root
            currentNode = self.root
            return self.insert_helper(currentNode, newNode)

    def insert_helper(self, currentNode, newNode):
        #base cases - when you find the key return True, when you dont return False
        if currentNode.key == newNode.key:
            currentNode.data = newNode.data

        #traversal - when it is greater go left, when less go right
        # when the current node key is greater than new node key
        elif currentNode.key > newNode.key:
            
            if currentNode.left == None:
                currentNode.left = newNode
            else:
                self.insert_helper(currentNode.left, newNode)
        
        # when the current node key is less than new node key
        elif currentNode.key < newNode.key:
            if currentNode.right == None:
                currentNode.right = newNode
            else:
                self.insert_helper(currentNode.right, newNode)
        
        
    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root == None:
            return None
        else:
            return self.find_min_helper()

    def find_min_helper(self):
        #finding min - left most leaf
        currentNode = self.root
        while currentNode.left != None:
            currentNode = currentNode.left
        min_tuple = (currentNode.key, currentNode.data)
        return min_tuple


    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root == None:
            return None
        else:
            return self.find_max_helper()
    
    def find_max_helper(self):
        #finding max - right most leaf
        currentNode = self.root
        while currentNode.right != None:
            currentNode = currentNode.right
        max_tuple = (currentNode.key, currentNode.data)
        return max_tuple


    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.root == None:
            return None
        else:
            currentNode = self.root
            return self.tree_height_helper(currentNode)

    def tree_height_helper(self, node):
        #base case
        if node == None:
            return -1

        #traverse through
        leftSubtree = self.tree_height_helper(node.left) + 1
        rightSubtree = self.tree_height_helper(node.right) + 1
        
        #compare left and right subtrees
        tallest = max(leftSubtree, rightSubtree)
        return tallest


    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.root == None:
            return []
        else:
            currentNode = self.root
            finalList = []
            return self.inorder_list_helper(currentNode, finalList)
    
    def inorder_list_helper(self, node, finalList):
        if node != None:
            self.inorder_list_helper(node.left, finalList)
            finalList.append(node.key)
            self.inorder_list_helper(node.right, finalList)
        return finalList


    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.root == None:
            return []
        else:
            currentNode = self.root
            finalList = []
            return self.preorder_list_helper(currentNode, finalList)

    def preorder_list_helper(self, node, finalList):
        if node != None:
            finalList.append(node.key)
            self.preorder_list_helper(node.left, finalList)
            self.preorder_list_helper(node.right, finalList)
        return finalList
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!

        #empty list
        if self.root == None:
            return []

        finalList = []
        #enqueue root
        q.enqueue(self.root)
        #while queue not empty
        while not q.is_empty():
            #dequeue node
            currentNode = q.dequeue()
            #process node
            finalList.append(currentNode.key)
            #enqueue children
            if currentNode.left != None:
                q.enqueue(currentNode.left)
            if currentNode.right != None:
                q.enqueue(currentNode.right)
        return finalList


        

