class Solution:
    def bellman_ford(self, n, edges, src):

        distances = [float("+inf")] * n
        st = [-1] * n

        distances[src] = 0
        st[src] = src

        for _ in range(n - 1): #!maximum V -1 upddates for each edge --> O(V * E)

            updates = False

            for u, v, weight in edges:
                if distances[u] < float("+inf") and distances[u] + weight < distances[v]:
                    updates = True 
                    distances[v] =  distances[u] + weight
                    st[v] = u
                
            if not updates:
                return distances, st
        
        for u, v, weight in edges:
                if distances[u] < float("+inf") and distances[u] + weight < distances[v]:
                    print("Cycle found!")
                    return None, None
        
        return distances, st

            


