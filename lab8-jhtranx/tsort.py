from sys import argv
from stack_array import *

class Vertex:

    def __init__(self):
        self.inDegree = 0
        self.adjList = []

    # def __repr__(self):
    #     return str(self.inDegree) + ' ' + str(self.adjList)

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility "tsort".  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''

    #theres a odd number of vertices in the list
    if len(vertices) % 2 != 0:
        raise ValueError("input contains an odd number of tokens")

    #there are no vertices at all
    if len(vertices) == 0:
        raise ValueError("input contains no edges")

    dict = {}
    #iterates every other index (first index of a pair)
    for i in range(0, len(vertices), 2):
        #checks if current vertex is already in the dictionary
        if vertices[i] in dict: #if vertex is in the dictionary

            if vertices[i + 1] not in dict: #if the second vertex of the pair does not exist
                dict[vertices[i + 1]] = Vertex() #create a new vertex object in the dictionary
                dict[vertices[i + 1]].inDegree += 1 #increase indegree by 1
                dict[vertices[i]].adjList.append(vertices[i + 1]) #append second vertex to first vertex's adj list

            elif vertices[i + 1] in dict: #if the second vertex of the pair does exist
                dict[vertices[i + 1]].inDegree += 1 #increase indegree by 1
                dict[vertices[i]].adjList.append(vertices[i + 1]) #append second vertex to first vertex's adj list

        elif vertices[i] not in dict: #if vertex is not in the dictionary
            dict[vertices[i]] = Vertex() #create a new vertex object in the dictionary

            if vertices[i + 1] not in dict: #if the second vertex of the pair does not exist
                dict[vertices[i + 1]] = Vertex() #create a new vertex object in the dictionary
                dict[vertices[i + 1]].inDegree += 1 #increase indegree by 1
                dict[vertices[i]].adjList.append(vertices[i + 1]) #append second vertex to first vertex's adj list

            elif vertices[i + 1] in dict: #if the second vertex of the pair does exist
                dict[vertices[i + 1]].inDegree += 1 #increase indegree by 1
                dict[vertices[i]].adjList.append(vertices[i + 1]) #append second vertex to first vertex's adj list
    # return dict
    #adjacently list done

    #prepwork for ordering
    stack = Stack(len(dict))
    orderList = []

    #iterate through dictionary
    for vertex in dict:
        if dict[vertex].inDegree == 0: #if vertex object has an indegree of 0
            stack.push(vertex) #push current vertex to stack

    #pop the stack when its not empty
    while not stack.is_empty():
        currentVertex = stack.pop()
        #iterate through adj list
        for vertex in dict[currentVertex].adjList:
            dict[vertex].inDegree -= 1 #reduce indegrees of adj list
            if dict[vertex].inDegree == 0: #if the current vertex indegree is zero
                stack.push(vertex) #push current vertex to stack
        orderList.append(currentVertex) #add current vertex to order list
        del dict[currentVertex] #delete popped vertex from dictionary

    #stack is empty

    #if stack is empty BUT dict is not
    if bool(dict):
        raise ValueError("input contains a cycle")

    #orderlist is complete
    orderString = "\n".join(orderList)
    return orderString


def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
