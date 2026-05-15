class Solution:
    #!O(ElogV) DIJKSTRA
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[] for _ in range(n)] 

        for u, v, time in times:
            graph[u - 1].append((v, time))
        
        min_heap = [(0, k)]
        visited = set()
        last = None


        while min_heap:

            curr_dist, u = heapq.heappop(min_heap)

            if u in visited:
                continue

            last = curr_dist
            visited.add(u)
            
            for neigh, time in graph[u - 1]:
                if neigh not in visited:
                    heapq.heappush(min_heap, (curr_dist + time, neigh))
                
        
        
        return last if len(visited) == n else -1




    