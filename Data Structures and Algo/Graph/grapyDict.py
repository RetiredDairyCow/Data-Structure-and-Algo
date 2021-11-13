from collections import defaultdict
#DFS uses stack (pop from top of stack)
#DFS: find graph cycle, to solve a maze, path finding
#BFS uses queue (pop from front)
#BFS application: build search index, GPS,  cycle detection in undirected graph
#path finidng algo also uses BFS

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.size = 6
    
    def addEdges(self, edge1, edge2):
        '''if it is a directed graph don't add edges for both vertex'''
        self.graph[edge1].append(edge2)
        self.graph[edge2].append(edge1)

    def detectCycleWrapper(self, startingVertex):
        if self.detectCycle(startingVertex) == True: 
            print('<- This is the cycle')
        else: 
            print('<- No Cycle found. This was the path taken')
    
    def detectCycle(self, vertex, parent=None, visited=set() ):
        '''Using DFS we check to see if an adjacent node is visited and if it is not the parent of current node
           We have detected the cycle'''

        visited.add(vertex)
        print(vertex,end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self.detectCycle(neighbor, vertex, visited): return True
            elif neighbor != parent: return True
        
        return False
        

    def DFS(self, vertex, visitedStack):
        """Recursive DFS"""
        #if vertex not in visitedStack:
        visitedStack.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.graph[vertex]:
            if neighbor not in visitedStack:
                self.DFS(neighbor, visitedStack)
    
    def DFS_Iterative(self, vertex, visited, stack=[]):
        stack.append(vertex)

        while stack:
            v = stack.pop()
            
            if v not in visited:
                print(v, end = ' ')
                visited.add(v)
           
            for n in reversed(self.graph[v]):
                if n not in visited:
                    stack.append(n)

    def BFS(self, vertex, visited):
        queue = []
        queue.append(vertex)
        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                print(v, end= ' ')
            
            for neighbor in (self.graph[v]):
                if neighbor not in visited:
                    queue.append(neighbor)
     


myGraph = Graph()
#myGraph.addEdges(0,1)
myGraph.addEdges(0,2)
myGraph.addEdges(2,1)
myGraph.addEdges(2,4)
myGraph.addEdges(2,5)
myGraph.addEdges(3,4)
print(myGraph.graph)

visited = set()
#myGraph.DFS_Iterative(2, visited)
#myGraph.BFS(0, visited)
myGraph.detectCycleWrapper(0)