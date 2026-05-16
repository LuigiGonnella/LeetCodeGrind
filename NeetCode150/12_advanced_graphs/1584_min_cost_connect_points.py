# #!O(E * logE), but in this case (dense graph) --> O(V^2logV)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        pq = [(0, points[0])]
        visited = set()
        tot_cost = 0

        while pq and len(visited) < len(points): #O(E)

            distance, node = heapq.heappop(pq)

            if tuple(node) in visited:
                continue
            
            visited.add(tuple(node))
            tot_cost += distance

            for neigh in points:
                if tuple(neigh) not in visited:
                    weight = abs(node[0] - neigh[0]) + abs(node[1] - neigh[1])
                    heapq.heappush(pq, (weight, neigh)) #O(logE)
        
        return tot_cost


#!O(V^2)
class Solution:
    # Strict O(V^2) Time | O(V) Space
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #INITIALIZATION
        n = len(points)

        distances = [float("+inf")] * n
        visited = [False] * n
        distances[0] = 0
        tot_cost = 0
       
        #INCLUDE EVERY NODE       
        for _ in range(n):

            curr_node = -1
            min_edge = float("+inf")

            #FIND THE NEAREST TO THE LAST INSERTED NODE
            for node in range(n):
                if not visited[node] and distances[node] < min_edge:
                    curr_node = node
                    min_edge = distances[node]
            
            #ADD IT TO THE SOLUTION
            visited[curr_node] = True
            tot_cost += min_edge

            #UPDATE ALL DISTANCES OF ANY OTHER (NOT ALREADY VISITED) NODE
            for next_node in range(n):

                if not visited[next_node]:
                    weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                    distances[next_node] = min(distances[next_node], weight)
        
        return tot_cost

