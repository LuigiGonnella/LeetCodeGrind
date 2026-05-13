
# #!O(V + E)
# #DFS CYCLE DETECTION AND CC COUNTING
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set() #since we do only 1 dfs run is ok to have a global set (no difference between visiting and visited), otherwise we would need a state 0-1-2

        def dfs(node, parent):
            if node in visited: #! CYCLE
                return False
    
            visited.add(node)

            for neigh in graph[node]:
                if neigh == parent: #undirected graph means that every edge is present in both directions, so skip if we already processed it
                    continue
                if not dfs(neigh, node):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n


#!O(V + E)
#DFS NODES AND EDGES COUNTING
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: #a tree has exactly n - 1 edges (means no cycles if it is connected, so now we must check connection)
            return False

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh)
               
        dfs(0)
        
        return len(visited) == n