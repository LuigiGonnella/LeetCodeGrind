
def find_articulation_points(graph, num_nodes):
    oldest = {node: -1 for node in range(num_nodes)} #oldest reachable node in DFS tree
    #cannot initialize to +inf oldest because the bridge check would always be true 
    # (in this case is still good because a leaf lead to a bridge by rule, but it is a bad habit)
    discovery = {node: -1 for node in range(num_nodes)} #discovery time during DFS
    children = {node: [] for node in range(num_nodes)} #DFS children
    timer = 0
    articulation_points = set()
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
                #if root has at least 2 children --> add
                children[node].append(neighbor)

                dfs(neighbor, node)

                #after precessing of neighbor 
                #  update oldest reachable node
                oldest[node] = min(oldest[node], oldest[neighbor])

                #!see if this neighbour (not root) would be disconnected without node
                if parent != -1 and oldest[neighbor] >= discovery[node]: #NOTE >= NOW!!
                    articulation_points.add(node)


            elif discovery[neighbor] < discovery[node]: #BACKWORD EDGE  
                #update oldest reachable node since we got a backward edge
                oldest[node] = min(oldest[node], discovery[neighbor])
        
        #!if root has at least 2 children --> add
        if parent == -1 and len(children[node]) >= 2:
            articulation_points.add(node)
    
    for node in range(num_nodes):
        if discovery[node] == -1:
            dfs(node, -1)
    
    return list(articulation_points)

