"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#!O(V + E)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        oldToNew[node] = Node(node.val) #used for both mapping old to new and marking visited nodes
        queue = deque([node])

        while queue:
            currNode = queue.popleft()
            

            for neigh in currNode.neighbors:
                if neigh not in oldToNew:
                    queue.append(neigh)
                    oldToNew[neigh] = Node(neigh.val)
                oldToNew[currNode].val = currNode.val
                oldToNew[currNode].neighbors.append(oldToNew[neigh])
                
        
        return oldToNew[node]
        
        