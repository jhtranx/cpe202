from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.color = None # color of the vertex object
        self.id = key # the name of the current vertex
        self.adjacent_to = [] # list of vertices that the current vertex is adj to
        self.visited = False
    
    # def __repr__(self):
    #     return (str(self.id) + " " + str(self.adjacent_to))

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''

        #prepwork
        self.graph = {} #create dictionary for vertices
        self.visited = [] # list of vertices that are visited
        vertices = [] #list of vertices used to make the graph

        #read into the file and append to list of vertices
        file = open(filename,"r") 
        Content = file.read()
        for line in Content.split():
            vertices.append(line)
        
        self.create_graph(vertices, self.graph)
        file.close()


    def create_graph(self, vertices, dict):
        #iterates every other index (first index of a pair)
        for i in range(0, len(vertices), 2):

            if vertices[i] not in dict: #if first vertex is not in the dictionary
                dict[vertices[i]] = Vertex(vertices[i]) #create a new first vertex object in the dictionary

            if vertices[i + 1] not in dict: #if the second vertex of the pair does not exist
                dict[vertices[i + 1]] = Vertex(vertices[i + 1]) #create a new second vertex object in the dictionary

            dict[vertices[i + 1]].adjacent_to.append(vertices[i])  #append first vertex to second vertex's adj list
            dict[vertices[i]].adjacent_to.append(vertices[i + 1])  #append second vertex to first vertex's adj list


    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)


    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph:
            return self.graph[key]
        return None


    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        #first add v2 to v1's adj list
        self.get_vertex(v1).adjacent_to.append(v2)
        #first add v1 to v2's adj list
        self.get_vertex(v2).adjacent_to.append(v1)


    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        #prepwork
        idList = []
        #for every key in the graph dictionary, append them into a list
        for id in self.graph.keys():
            idList.append(id)
        
        #sort list in order
        idList.sort()
        return idList


    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        #prepwork
        self.reset_visit()
        finalList = []
        self.visited = [] #reset visited vertices

        vertexList = self.get_vertices()

        for vertex in vertexList:
            if not self.get_vertex(vertex).visited:
                list = self.depth_first_search(vertex)
                # print(list)
                list.sort()
                # print(list)
                finalList.append(list)

        return finalList


    def depth_first_search(self, vertex):
        '''vertex is a str'''
        #prepwork
        stack = Stack(len(self.graph)) #create stack
        visitedList = []

        currentVertex = vertex
        visitedList.append(currentVertex)
        self.get_vertex(currentVertex).visited = True
        stack.push(currentVertex) #push the current vertex onto stack

        while not stack.is_empty():

            while self.find_notvisited(currentVertex) != None: #this means that there is an open spot
                currentVertex = self.find_notvisited(currentVertex)
                self.get_vertex(currentVertex).visited = True # set the current vertex to visited
                visitedList.append(currentVertex)
                self.visited.append(currentVertex)
                stack.push(currentVertex) #push the current vertex onto stack

            #if it at a dead end
            else:
                stack.pop() # pop the stack
                if not stack.is_empty():
                    currentVertex = stack.peek() 
                else:
                    return visitedList
        
        # return visitedList


    def find_notvisited(self, vertex):
        '''check if the current vertex is a dead end or not
        if theres is a vertex that is open return it
        if there is none, return None'''
        currentAdjList = self.get_vertex(vertex).adjacent_to #create adjlist of the current vertex

        #for every vertex in the list
        for vertex in currentAdjList:
            #if the vertex has not been visited, return it
            if not self.get_vertex(vertex).visited:
                return vertex
        return None #return none if all of them are visited
    
    
    def reset_visit(self):
        for vertex in self.get_vertices():
            self.get_vertex(vertex).visited = False


    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        #prepwork
        componentList = self.conn_components()
        self.reset_visit()
        
        for component in componentList:
            vertex = component[0] #set vertex to the first vertex in the component list
            boolean = self.breath_first_search(vertex) #if the component is biparate or not true or false

            #if the component is not biparate
            if boolean == False: 
                return False

        return True
        


    def breath_first_search(self, vertex):
        #prepwork
        queue = Queue(len(self.graph)) #create a queue that is the size of the vertices in the graph
        currentVertex = vertex
        self.get_vertex(currentVertex).color = 'Black'
        queue.enqueue(currentVertex)

        while not queue.is_empty():
            #dequeue to get vertex
            currentVertex = queue.dequeue()
            #set a variable to the current vertex's adjList
            currentAdjList = self.get_vertex(currentVertex).adjacent_to 

            #enqueue all of its children
            for vertex in currentAdjList:
    
                if not self.get_vertex(vertex).visited: #if the color is None it means it hasnt been visited yet
                    #set visited to True
                    self.get_vertex(vertex).visited = True
                    #enqueue the vertex into the queue
                    queue.enqueue(vertex)

                    #if the parent of the vertex color is Red
                    if self.get_vertex(currentVertex).color == 'Red':
                        self.get_vertex(vertex).color = 'Black' #set current node color to black
                    elif self.get_vertex(currentVertex).color == 'Black':
                        self.get_vertex(vertex).color = 'Red' #set current node color to black

                #if the child does has the same color as its parent it means it is False
                elif self.get_vertex(vertex).color == self.get_vertex(currentVertex).color:
                    return False
        
        return True





