
#!O(ElogE) = O(ElogV)
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