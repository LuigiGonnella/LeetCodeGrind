
def find_bridges(graph, num_nodes):
    

    oldest = {node: -1 for node in range(num_nodes)} #oldest reachable node in DFS tree
    #cannot initialize to +inf oldest because the bridge check would always be true 
    # (in this case is still good because a leaf lead to a bridge by rule, but it is a bad habit)
    discovery = {node: -1 for node in range(num_nodes)} #discovery time during DFS
    timer = 0
    bridges = []
    def dfs(node, parent):
        nonlocal timer

        #initialize both
        discovery[node] = timer
        oldest[node] = timer #minimum reachable time is this time at the beginning (the node itself)
        timer += 1

        for neighbor in graph[node]:

            #!------ ONLY FOR NOT DIRECTED GRAPHS -------
            if neighbor == parent:
                continue
            #!-------------------------------------------

            if discovery[neighbor] == -1: #TREE EDGE
                dfs(neighbor, node)

                #after precessing of neighbor 
                #  update oldest reachable node
                oldest[node] = min(oldest[node], oldest[neighbor])

                #see if this neighbour would be disconnected without this (node, neighbor) edge
                if oldest[neighbor] > discovery[node]:
                    bridges.append((node, neighbor))


            elif discovery[neighbor] < discovery[node]: #BACKWORD EDGE  
                #update oldest reachable node since we got a backward edge
                oldest[node] = min(oldest[node], discovery[neighbor])
    
    for node in range(num_nodes):
        if discovery[node] == -1:
            dfs(node, -1)

    return bridges