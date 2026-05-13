
# #!O(V + E)
# #KHAN'S ALGORITHM BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:   
        res = []
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for dst, src in prerequisites:
            graph[src].append(dst)
            in_degree[dst] += 1
        
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])

        while queue:
            course = queue.popleft()
            res.append(course)
            
            for neigh in graph[course]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        
        return res if len(res) == numCourses else []
        

#!O(V + E) 
# TOPOLOGICAL SORT --> DETECT CYCLE DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [course for course in range(numCourses)]

        graph = [[] for _ in range(numCourses)]


        for dst, src in prerequisites:
            graph[src].append(dst)


        inv_topological = [] #for a DAG there is only 1 topological sort
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1: #!CYCLE
                return False
    
            if state[node] == 2:
                return True

            state[node] = 1

            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
                         

            state[node] = 2
            inv_topological.append(node)
            return True

        for node in range(len(graph)): 
            if state[node] == 0 and not dfs(node):
                return []
        
        return inv_topological[::-1]
        

        