

#!O(V + E))
class Solution:
    def dijsktra(self, n, edges, src): #find minimum distance from SRC to any other node

        # 1. Build the Adjacency List
        graph = defaultdict(list)

        for u, v, weight in edges:
            graph[u].append((v, weight)) #directed


        # 2. Obtain topological order
        visited = [False] * n
        reverse_topological = []
        def dfs(node): #!O(V + E)
            if visited[node]:
                return
            
            visited[node] = True

            for neigh in graph[node]:
                dfs(neigh)
            
            reverse_topological.append(node)
        
        for node in range(n):
            if not visited[node]:
                dfs(node)
        
        topological_order = reversed(reverse_topological)
        
        
        # 3. Initialize Distance and Spanning Tree/Parent arrays
        distances = [float("+inf") for _ in range(n)]
        st = [-1 for _ in range(n)]

        distances[src] = 0
        st[src] = src 

        for node in topological_order: #!O(V + E) --> loops ovber V and looks to all E once

            if distances[node] < float("+inf"): #if a node is unreachable, do not consider its neighbors
                for neigh, weight in graph[node]:
                    # Relaxation Step: Have we found a strictly shorter path to neigh?
                    if distances[node] + weight < distances[neigh]: #for maximum paths, just put > instead of < and initialize distances to -INF 
                        distances[neigh] = distances[node] + weight
                        parents[neigh] = node
        
        return distances, st
