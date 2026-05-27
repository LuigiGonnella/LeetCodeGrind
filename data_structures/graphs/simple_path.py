


path = []
visited = set()

def find_simple_path(graph, nodeA, nodeB):

    path.append(nodeA)
    visited.add(nodeA)

    if nodeA == nodeB:
        return True
    
    for node in graph.get(nodeA, []):  #adjacency list in dict
        if node not in visited and find_simple_path(graph, node, nodeB):
            return True
    
    path.pop() #backtrack
    
    return False


#in main:
#if find_simple_path(graph, nodeA, nodeB):
    return path
