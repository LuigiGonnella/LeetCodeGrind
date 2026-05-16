
#!O(ElogE) = O(ElogV, but for dense graphs this is O(V^2logV), so it is better the matrix solution --> O(V^2)
class Solution:
    def minimumSpanningTree(self, n, edges):

        # Step 1: Build the Adjacency List
        # Since it's an undirected graph, we add the edge in both directions.
        graph = defaultdict(list) #!O(V + E) space
        for u, v, weight in edges:
            graph[u].append((weight, v))
            graph[v].append((weight, u))
        
        # Step 2: Initialize the Priority Queue (Min-Heap) and Visited set
        # Heap stores tuples of (weight, node). Start at node 0 with 0 weight.
        min_heap = [(0, 0)] #!O(E) space
        min_weight = 0
        visited = set()

        # Step 3: The Core Algorithm Loop
        # We stop early if we have visited all 'n' nodes.
        while min_heap and len(visited) < n: #!O(E) --> maximum E edges in HEAP
            
            # Pop the smallest available edge that connects the MST to a new node
            weight, node = heapq.heappop(min_heap) #!O(logE)
            
            # If the node is already in our MST, ignore it and continue
            if node in visited:
                continue
            
            # Step 4: Add node to the MST --> only if it has the smallest distance and it was not visited before
            visited.add(node)
            min_weight += weight
            

            for weight, neigh in graph[node]: #insert all neighbors in queue, it can be inserted multiple times, even if ALREADY visited, since it can be traversed by multiple paths **BEFORE** we pop it
                if neigh not in visited:
                    heapq.heappush(min_heap, (weight, neigh))
                    

        # Step 5: Verify the tree
        return min_weight if len(visited) == n else -1


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