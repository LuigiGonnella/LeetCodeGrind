

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
