
#!O(ElogE)
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

