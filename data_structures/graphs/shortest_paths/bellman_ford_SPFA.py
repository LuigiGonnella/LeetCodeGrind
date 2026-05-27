from collections import defaultdict, deque
from typing import List, Tuple, Optional

class Solution:
    def spfa(self, n: int, edges: List[List[int]], src: int) -> Tuple[Optional[List[int]], Optional[List[int]]]:
        # 1. Build Adjacency List
        adj = defaultdict(list)
        for u, v, weight in edges:
            adj[u].append((v, weight))
            
        # 2. Initialize Arrays
        distances = [float('inf')] * n
        parents = [-1] * n
        distances[src] = 0
        
        # 3. Queue and Tracking arrays for SPFA
        q = deque([src])
        in_queue = [False] * n
        in_queue[src] = True
        
        # Array to track how many times a node is popped (for negative cycle detection)
        update_count = [0] * n 
        
        # 4. The Algorithm
        while q:
            u = q.popleft()
            in_queue[u] = False  # It's out of the queue, so we can add it again later if needed
            
            for v, weight in adj[u]:
                # Relaxation step
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    parents[v] = u
                    
                    # Only add to queue if it's not already sitting in there waiting to be processed!
                    if not in_queue[v]:
                        q.append(v)
                        in_queue[v] = True
                        
                        # Negative Cycle Detection: 
                        # In a normal graph, a node should never be updated more than V-1 times.
                        update_count[v] += 1
                        if update_count[v] >= n:
                            print("Negative cycle found!")
                            return None, None
                            
        return distances, parents