
#O(N) time and space
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        if not rooms:
            return True
        
        n = len(rooms)
        visited = [False] * n
        n_visited = 0
        def dfs(i):
            nonlocal n_visited

            visited[i] = True
            n_visited += 1
            for neigh in rooms[i]:
                if not visited[neigh]:
                    dfs(neigh)
        
        dfs(0)

        return n_visited == n