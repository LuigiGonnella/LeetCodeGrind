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


#in main:
#if find_eulero_path(graph, nodeA, nodeB):
    return path
