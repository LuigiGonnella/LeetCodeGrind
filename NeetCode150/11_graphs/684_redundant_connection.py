
#!O(E * (E + V))
#DFS
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(len(edges))]

        for u, v in edges:
            graph[u - 1].append(v)
            graph[v - 1].append(u)
        
        redundants = set()
        res = False
        def dfs(node, parent, state):
            nonlocal res
            nonlocal redundants
        
            if state[node - 1] == 2:
                return

            state[node - 1] = 1

            for neigh in graph[node - 1]:
                if not res:
                    if neigh == parent:
                        continue
                    
                    if state[neigh - 1] == 0:
                        dfs(neigh, node, state)

                    elif state[neigh - 1] == 1: #!CYCLE, even if was enough to have only the visited one, sine this is for sure a tree (connected)
                        redundants.add((node, neigh))
                        redundants.add((neigh, node))
                        return
            
            state[node - 1] = 2
                    
        
        for node in range(len(edges)):
            dfs(node + 1, -1, [0] * len(edges))
        
        for i in range(len(edges) - 1, -1, -1):
            edge = tuple(edges[i])
            if edge in redundants:
                return list(edge)

#!O(V + E)
#UNION-FIND
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        #weighted quick union
        st = [node for node in range(n)]
        size = [1 for _ in range(n)]

        def find(node): #O(N)
            if node != st[node]:
                st[node] = find(st[node]) #path compression makes find complexity amortized by an ALPHA factor
                # --> O(alpha*N) which ispractically O(1)
            return st[node]
        
        def union(small, large):
            st[small] = st[large]
            size[large] += size[small]
            

        for u, v in edges:
            pu = find(u - 1)
            pv = find(v - 1)

            if pu == pv:
                return [u, v]

            if size[pu - 1] < size[pv - 1]:
                union(pu, pv)
            else:
                union(pv, pu)



















