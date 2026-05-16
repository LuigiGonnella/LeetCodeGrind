
#!O(E), in this case with sort --> O(ElogE)
#HIERHJOLZER'S ALGORITHM
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        tickets.sort(reverse = True)
        for src, dst in tickets:
            graph[src].append(dst)
        
        path = []
        def dfs(node):
     
            while graph[node]:
                dst = graph[node].pop()
                dfs(dst)
            
            path.append(node)                    

            
        dfs("JFK")
        return path[::-1]



#DFS handling the duplicate esged (multigraphs)
#!O(E*V)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:    
        graph = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            graph[src].append(dst)

        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            
            if node not in graph:
                return False
            
            tmp = list(graph[node])
            for i, neigh in enumerate(tmp):
                graph[node].pop(i)
                res.append(neigh)
                if dfs(neigh):
                    return True
                graph[node].insert(i, neigh)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res 

