#Implementation of graphs using adjacency matrix

class Graph():
    def __init__(self, size):
        self.adjMatrix = [[0]*size for i in range(size)]
        self.size = size
        

    def print_matrix(self):
        for row in self.adjMatrix:
            for value in row:
                print('{:4}'.format(value),end=" ")
            print('\n')
    

    def addEdge(self, vertex1, vertex2):
        if (vertex1 == vertex2):
            print("Can't have same edges")
            return
        #since it's undirected graph add edges for both cases
        self.adjMatrix[vertex1][vertex2] = 1
        self.adjMatrix[vertex2][vertex1] = 1
    
    def deleteEdge(self, vertex1, vertex2):
        if (self.adjMatrix[vertex1][vertex2] == 0):
            print("No edges to delete")
            return
        self.adjMatrix[vertex1][vertex2] = 0
        self.adjMatrix[vertex2][vertex1] = 0
    
    def DFS(self, vertex, visitedStack):
        print(vertex, end=' ')
        visitedStack.add(vertex)
        
        #for everynode, check connected edges and if not in visited, add it to visited
        for i in range(self.size):
            if self.adjMatrix[vertex][i] == 1 and (i not in visitedStack):
                self.DFS(i, visitedStack)
            
    def BFS(self, vertex, visitedQueue)
        pass

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0,3)
g.addEdge(2,3)
g.print_matrix()
visitedStack = set() 
visitedQueue = []
#g.DFS(0, visitedStack)
g.BFS(0, visitedQueue)