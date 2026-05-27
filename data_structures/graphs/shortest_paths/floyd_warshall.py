class Solution:
    def floydWarshall(self, n: int, edges: list[list[int]]) -> list[list[float]]:
        # 1. Initialize a 2D matrix with Infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # 2. Distance from a node to itself is 0
        for i in range(n):
            dist[i][i] = 0
            
        # 3. Populate initial known edge weights
        for u, v, weight in edges:
            dist[u][v] = weight
            # dist[v][u] = weight  
            
        # 4. The Algorithm (3 nested loops)
        # Note: 'k' (the middleman) MUST be the outermost loop!
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # If going through 'k' is strictly cheaper, update the distance
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        return dist