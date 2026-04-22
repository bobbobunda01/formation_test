from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph=defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def __dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        
        for nb in self.graph[v]:
            if nb not in visited:
                self.__dfs_util(nb, visited)
    
    def dfs(self, v):
        visited=set()
        self.__dfs_util(v, visited)

g=Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

print("DSF à partir du noeud:")
g.dfs(0)