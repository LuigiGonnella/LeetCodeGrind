#if we want to maintaing the parent tree during DFS

def stateful_dfs(num_nodes, edges):
    graph = {node: [] for node in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)
        #only if not oriented
        graph[v].append(u)

    #0 --> UNVISITED (visit starting --> PRE-ORDER)
    #1 --> VISITING
    #2 --> VISITED (visit terminated --> POST-ORDER)
    state = {node: 0 for node in range(num_nodes)}
    parent = {node: node for node in range(num_nodes)}

    def dfs(currNode):
        
        if state[currNode] == 1: 
            #!We hit a node currently in our active path -> BACK EDGE -> CYCLE!
            return 
        
        if state[currNode] == 2: 
            # We hit a node we already fully explored -> CROSS OR FORWARD EDGE EDGE
            return 

        # We hit a node not yet explored -> TREE EDGE
        # Mark as Visiting
        state[currNode] = 1

        for node in graph[currNode]:
            #!set parent
            parent[node] = currNode
            if state[node] == 1:
                print(f" {currNode} --> {node} is a BACKWARD EDGE --> CYCLE FOUND!")
            elif state[node] == 2:
                print(f" {currNode} --> {node} is a CROSS OR FORWARD EDGE EDGE")
            else:
                print(f" {currNode} --> {node} is a TREE EDGE")
                
            #this call will not immediately return only if state[node] == 0
            #so it make sense to put it only in the "else" branch
            #but more generally we always want to recurr and then return in the next call depending on our task
            dfs(node)
        
        #process is finished
        state[currNode] = 2
    
    for node in range(num_nodes):
        if state[node] == 0:
            dfs(node)
            