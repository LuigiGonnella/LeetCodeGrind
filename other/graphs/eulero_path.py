from collections import defaultdict

#!DFS simple case (no multigraph) --> O(E!)

path = []

visited = set()

E = 10

def find_eulero_path(graph, nodeSource, nodeDest):
    path.append(nodeSource)

    if nodeSource == nodeDest and len(path) == E + 1:

        return True

    for node in graph.get(nodeSource, []):  #adjacency list in dict

        if (nodeSource, node) not in visited:

            visited.add((nodeSource, node))

            if find_eulero_path(graph, node, nodeDest):

                return True

            visited.remove((nodeSource, node)) #backtrack

    path.pop() #backtrack

    return False

#!DFS HANDLING MULTIGRAPHS --> O(E*V)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res

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