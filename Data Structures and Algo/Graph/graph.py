#Graph data structure 
#Graph consists of nodes (or vertices) elements and edges connecting the notes
#Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
#Space Complexity: O(V). Since an extra visited array is needed of size V 

class AdjacentNodes: 
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.totalVertices = vertices
        self.graph = self.totalVertices * [None] #total size of array which in turn will hold a linked list
        
        for i in range(self.totalVertices):
            self.graph[i] = AdjacentNodes(i)
            
    def addEdge(self, source, destination):
        '''Make vertex node and add it to graph[source].next
           Then do the same for graph[destination].next'''
        node = AdjacentNodes(destination)
        temp = self.graph[source]
        while temp.next:
            temp = temp.next
        temp.next = node

        node = AdjacentNodes(source)
        temp = self.graph[destination]
        while temp.next:
            temp = temp.next
        temp.next = node

    def printGraph(self):
        for i in range(self.totalVertices):
            print("Connected edges at vertex {} are".format(i), end="")
            temp = self.graph[i].next
            while temp:
                print("-> {}".format(temp.vertex), end="")
                temp = temp.next

            print("\n") 

    def DFS(self, vertex, visited, neighborStack=[]):
        '''Start with a vertex. Add it to visited stack. 
           Find it's neighbors and add the first one to the visited stack if it's not already visited. 
           Repeat'''
        if not visited[vertex]:
            visited[vertex] = True
            print(vertex, end=' ')
            temp = self.graph[vertex].next #since graph[vertex] is the actual vertex node. We want to check the edges to the node
            while temp: 
                neighborStack.append(temp.vertex)
                temp = temp.next
                self.DFS(neighborStack.pop(0), visited, neighborStack)
        
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2,1)
g.addEdge(2,4)
g.addEdge(3,4)
g.printGraph()
visitedStack =  [False]*g.totalVertices 
g.DFS(4, visitedStack)


""" # Different way to do it. Found it online. 
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5') """