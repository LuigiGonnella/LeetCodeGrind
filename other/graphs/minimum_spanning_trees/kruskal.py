class UnionFind: #!O(V) space
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, node): #!O(alpha * V)
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        
        else:
            return node
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q: #already connected
            return False

        if self.size[root_p] < self.size[root_q]:
            self.size[root_q] += self.size[root_p]
            self.parent[root_p] = root_q
        else:
            self.size[root_p] += self.size[root_q]
            self.parent[root_q] = root_p

        return True 
    
class Solution:
    def minimumSpanningTree(self, n, edges): #edges is list of [u, v, weight] lists

        #!1) Sort edges by ascending weight --> O(ElogE) = O(ElogV)
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        min_weight = 0
        edges_used = 0

        #!2) iterate through sorted edges --> O(E*alpha*V)
        for u, v, weight in edges: 
            if uf.union(u, v): #True if they were on different components
                min_weight += weight
                edges_used += 1

            if edges_used == n - 1: #all nodes traversed
                break    
        
        if edges_used != n - 1: #if not connected the edges would be < n - 1, so we can add this check before returning
            return -1
        
        return min_weight #assuming a solution exist (graph was CONNECTED, ACYCLIC, UNDIRECTED)



