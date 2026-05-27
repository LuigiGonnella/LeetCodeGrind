
def basic_dfs(num_nodes, edges):
    graph = {node: [] for node in range(num_nodes)}
    for u, v in edges:
        graph[u].append(v)
        #only if not oriented
        graph[v].append(u)
    


    visited = set()
    def dfs(currNode): #!pre-order visit   
        visited.add(currNode)

        for node in graph[currNode]:
            if node not in visited:
                print(f" NODE {currNode} --> NODE {node}")
                dfs(node)
    
    for node in range(num_nodes):
        if node not in visited:
            dfs(node)