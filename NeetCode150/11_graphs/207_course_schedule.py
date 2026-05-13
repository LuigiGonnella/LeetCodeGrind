#!O(V + E) 
# DETECT CYCLE DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #construct a DAG and if is it possible to visit all the nodes starting from any SOURCE NODES --> True, otherwise --> False
        if not prerequisites:
            return True

        graph = [[] for _ in range(numCourses)]


        for dst, src in prerequisites:
            graph[src].append(dst)
  
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1: #!CYCLE
                return False
    
            if state[node] == 2:
                return True

            state[node] = 1

            for neigh in graph[node]:
                #! Only recursively visit if all prerequisites are met
                if not dfs(neigh):
                    return False
                         

            state[node] = 2
            return True

        for node in range(len(graph)): 
            if state[node] == 0 and not dfs(node):
                return False
        
        return True
        




#!O(V + E) (because of global visited, instead if the visited set was local  --> quadratic complexity)
# KHAN'S ALGORITHM DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #construct a DAG and if is it possible to visit all the nodes starting from any SOURCE NODES --> True, otherwise --> False
        if not prerequisites:
            return True

        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        nodes = set() #track ALL NODES in graph

        for dst, src in prerequisites:
            graph[src].append(dst)
            in_degree[dst] += 1
            nodes.add(src)
            nodes.add(dst)
        


        visited = set() #global visited to see if I visit all during the DFSs (I DO NOT need to visit all of them in only ONE DFS)

        def dfs(node):
    
            visited.add(node)

            for neigh in graph[node]:
                in_degree[neigh] -= 1
                #! Only recursively visit if all prerequisites are met
                if in_degree[neigh] == 0 and neigh not in visited:
                    dfs(neigh)      


        for node in range(len(graph)): #for EACH COURSE 
            #! Start a DFS chain only from nodes with NO prerequisites
            if in_degree[node] == 0 and len(graph[node]) > 0 and node not in visited: #len(graph[node]) > 0 is required to visit only nodes actually present in the graph
                dfs(node)
        
        return len(visited) == len(nodes)
        
        


# #!O(V + E) 
# # KHAN'S ALGORITHM BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:    
        if not prerequisites:
            return True

        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses


        for dst, src in prerequisites:
            graph[src].append(dst)
            in_degree[dst] += 1

        
        courses_taken = 0
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        #we don't need visited mark because if a course is not in the graph it will be considered taken and then skipped
        #and if a course has already beeen visited we will never visit it again (DAG), in fact if there is a cycle in_degree will never be 0
        while q:
            curr = q.popleft()
            courses_taken += 1
            
            for neigh in graph[curr]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)
        
        
        return courses_taken == numCourses









        