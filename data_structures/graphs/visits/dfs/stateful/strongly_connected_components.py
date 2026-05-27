#make sense only for DIRECTED GRAPHF (for not directed CC are always STRONG by definition)

def strongly_connected_components(graph, num_nodes):

    #KOSARAJU ALGORITHM

    #1) REVERSE GRAPH
    def reverseGraph(graph):
        graphT = {node : [] for node in graph}

        for node in graph:
            for neigh in graph[node]:
                graphT[neigh].append(node)
        
        return graphT



    graphT = reverseGraph(graph)

    #2) TOPOLOGICAL SORT ON GRAPHT
    inverted_topological_sort = []
    visited = {node: 0 for node in graphT}
    def get_topological_sort(node):

        visited[node] = 1

        for neigh in graphT[node]:
            if not visited[neigh]:
                get_topological_sort(neigh)
        
        inverted_topological_sort.append(node)
    
    for node in range(num_nodes):
        if not visited[node]:
            get_topological_sort(node)



    topological_sort = inverted_topological_sort[::-1]

    #3) DFS ON GRAPH ACCORDING TOPOLOGICAL SORT ON GRAPHT COUNTING CC
    components = {}
    cc = -1
    visited = {node: 0 for node in graph}
    def dfs(node):
        if cc not in components:
            components[cc] = []
        
        components[cc].append(node)
        visited[node] = 1

        for neigh in graph[node]:
            if not visited[neigh]:
                dfs(neigh)
    
    for node in topological_sort:
        if not visited[node]:
            cc += 1
            dfs(node)
    
    #4) PRINT STRONGLY CONNECTED COMPONENTS
    for comp in components:
        print(f"COMPONENT {comp}: {components[comp]}")









