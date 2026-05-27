path = []
visited = set()
V = 10

#!O(V!)
#backtracking
def find_hamilton_path(graph, nodeA, nodeB):

    path.append(nodeA)
    visited.add(nodeA)

    if nodeA == nodeB:
        if len(path) == V:
            return True
    
    else:
        for node in graph.get(nodeA, []):  #adjacency list in dict
            if node not in visited and find_hamilton_path(graph, node, nodeB):
                return True
    
    path.pop() #backtrack
    visited.remove(nodeA) #backtrack
    
    return False


#in main:
#if find_hamilton_path(graph, nodeA, nodeB):
    return path


from functools import cache
from collections import defaultdict

#!O(V^2*2^V)
#DP
class Solution:
    def hasHamiltonianPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) # Assuming undirected
            
        # A bitmask where all 'n' bits are set to 1 (e.g., n=4 -> 1111 in binary -> 15)
        # This represents the state where EVERY node is visited.
        TARGET_MASK = (1 << n) - 1
        
        # @cache automatically memoizes the inputs!
        @cache
        def dfs(current_node, visited_mask):
            # Base Case: We reached the destination
            if current_node == end:
                # Did we visit exactly 'n' nodes?
                return visited_mask == TARGET_MASK
                
            # Try all neighbors
            for neigh in graph[current_node]:
                # Check if the 'neigh' bit is 0 (unvisited)
                if not (visited_mask & (1 << neigh)):
                    
                    # Flip the 'neigh' bit to 1 and recurse
                    new_mask = visited_mask | (1 << neigh)
                    
                    if dfs(neigh, new_mask): #if this is False the "backtrack" will be automatic since the parent's visited_mask is unaltered
                        return True
                        
            return False

        # Start the DFS at 'start' node, with the 'start' bit set to 1
        return dfs(start, 1 << start)