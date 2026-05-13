
#!O(E + V)
#DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        visited = [0] * n
        def dfs(node):

            visited[node] = 1

            for neigh in graph[node]:
                if not visited[neigh]:
                    dfs(neigh)

        cc = 0

        for node in range(n):
            if not visited[node]:
                dfs(node)
                cc += 1
        
        return cc


#!O(E + V)
#BFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [0] * n
        
        def bfs(node):
            q = deque([node])
            visited[node] = 1

            while q:
                curr = q.popleft()
                
                for neigh in graph[curr]:
                    if not visited[neigh]:
                        visited[neigh] = 1
                        bfs(neigh)
        
        cc = 0

        for node in range(n):
            if not visited[node]:
                bfs(node)
                cc += 1
        return cc

