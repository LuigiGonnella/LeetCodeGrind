

#Time Complexity: O(E * K log(V * K))
# The Queue Size: In the worst-case scenario, every single node could be added to the priority queue up to K times 
# (once for each possible number of stops, 0 through K). 
# This means the priority queue can grow to a maximum size of V*K.
# Heap Operations: Popping from or pushing to a heap of that size takes O(log(V * K)) time.
# Edge Relaxations: Because we can visit each node up to K times, we might also evaluate each of its outgoing edges up to K times. 
# Thus, we process at most E * K edges.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for s, d, weight in flights:
            graph[s].append((d, weight))
        
        min_path = {}
        pq = [(0, src, 0)]

        while pq:
            cost, node, len_path = heapq.heappop(pq)
            
            if node == dst:
                return cost

            if (node in min_path and min_path[node] <= len_path) or len_path >= (k + 1): #add to solution only if within k stops
                continue

            min_path[node] = len_path

            for neigh, new_cost in graph[node]:
                heapq.heappush(pq, (new_cost + cost, neigh, len_path + 1))


        return -1

