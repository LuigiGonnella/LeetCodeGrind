from collections import defaultdict

#!simple case (no multigraph) --> O(E!)
def find_eulero_path(graph, start_node):
    # 'graph' should be a dictionary of lists: { u: [v1, v2, ...] }
    path = []
    
    def dfs(node):
        # As long as there are unused outgoing edges from this node
        while graph[node]:
            # Pop the edge so it is permanently removed (solves the duplicate edge issue!)
            next_node = graph[node].pop()
            dfs(next_node)
            
        # We only append to the path when we are completely stuck
        path.append(node)
        
    dfs(start_node)
    
    # Hierholzer's builds the path in post-order, so we must reverse it
    return path[::-1]

# Example Usage:
# graph = { 'A': ['B', 'C'], 'B': ['A'], 'C': [] }
# final_path = find_eulero_path(graph, 'A')

#!GENERAEL OPTIMAL CASE --> HIERHOLZER'S ALGORITHM --> O(E)
from collections import defaultdict

def find_eulero_path(graph, start_node):
    # 'graph' should be a dictionary of lists: { u: [v1, v2, ...] }
    path = []
    
    def dfs(node):
        # As long as there are unused outgoing edges from this node
        while graph[node]:
            # Pop the edge so it is permanently removed (solves the duplicate edge issue!)
            next_node = graph[node].pop()
            dfs(next_node)
            
        # We only append to the path when we are completely stuck
        path.append(node)
        
    dfs(start_node)
    
    # Hierholzer's builds the path in post-order, so we must reverse it
    return path[::-1]

# Example Usage:
# graph = { 'A': ['B', 'C'], 'B': ['A'], 'C': [] }
# final_path = find_eulero_path(graph, 'A')