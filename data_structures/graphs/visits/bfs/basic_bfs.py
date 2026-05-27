from collections import deque

def basic_bfs(graph, num_nodes, start_node):


    visited = {node: 0 for node in range(num_nodes)}
    #distances will always have the minimum distance from the start_node to any other node 
    # in terms of NUMBER of EDGES (so it does not apply to WEIGHTED EDGES --> here we apply DIJKSTRA if no negative weights and BELLMAN-FORD otherwise)
    distances = {node: 0 for node in range(num_nodes)}

    #to reconstruct the BFS tree
    parent = {node: -1 for node in range(num_nodes)}

    queue = deque([start_node])
    visited[start_node] = 1

    while queue:
        currNode = queue.popleft()

        for neigh in graph[currNode]:
            if not visited[neigh]:

                visited[neigh] = 1
                parent[neigh] = currNode
                distances[neigh] = distances[currNode] + 1

                queue.append(neigh)




    #reconstruct BFS TREE
    for node in range(num_nodes):
        if node != start_node:
            print(f"NODES {node}'S PARENT IS {parent[node]}")
    
    #reconstruct distances
    for node in range(num_nodes):
        if node != start_node:
            print(f"DISTANCE NODE {node} - START IS {distances[node]}")