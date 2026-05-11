path = []
visited = set()
V = 10

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
