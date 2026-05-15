

#!O(ElogE) = O(ElogV)
class Solution:
    def dijsktra(self, n, edges, src): #find minimum distance from SRC to any other node

        # 1. Build the Adjacency List
        graph = defaultdict(list)

        for u, v, weight in edges:
            graph[u].append((v, weight)) #directed
        
        # 2. Initialize Distance and Spanning Tree/Parent arrays
        distances = [float("+inf") for _ in range(n)]
        st = [-1 for _ in range(n)]

        distances[src] = 0
        st[src] = src 

        min_heap = [(0, src)]

        while min_heap: #maximum E iterations

            distance, node = heapq.heapop(min_heap) #!O(logE)

            # OPTIMIZATION (Lazy Deletion):
            if distance > distances[node]: #old entry
                continue

            for neigh, weight in graph[node]:
                # Relaxation Step: Have we found a strictly shorter path to neigh?
                if distances[node] + weight < distances[neigh]: 
                    distances[neigh] = distances[node] + weight
                    parents[neigh] = node
                    # Push the newly found better distance to the heap --> we have only REACHABLE nodes (so no need to check if distance is < +INF)
                    heapq.heappush(min_heap, (distances[neigh], neigh)) #!O(logE)
        
        return distances, st

#alternative (use set instead of distances) --> this will insert potentially HUGE edges in heap since we do not do relaxation, but then we will skip them
visited = set()
class Solution:
    def dijsktra(self, times: List[List[int]], n: int, k: int) -> int:
        # Build 0-indexed graph for 1-indexed nodes
        graph = [[] for _ in range(n)] 
        for u, v, time in times:
            graph[u - 1].append((v, time))
        
        # min_heap stores (accumulated_time, node)
        min_heap = [(0, k)]
        visited = set()
        last = 0

        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)

            # The "Lazy Deletion" catch
            if u in visited:
                continue

            # Lock in the visited node and update the maximum shortest path
            visited.add(u)
            last = curr_dist
            
            for neigh, time in graph[u - 1]:
                if neigh not in visited:
                    heapq.heappush(min_heap, (curr_dist + time, neigh))
                
        # If we visited all 'n' nodes, 'last' holds the time the final node was reached
        return last if len(visited) == n else -1