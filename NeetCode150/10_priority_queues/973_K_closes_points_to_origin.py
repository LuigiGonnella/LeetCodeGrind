
#!O(N + KlogN)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(p[0]**2 + p[1]**2, p) for p in points]
        heapq.heapify(min_heap) #O(N)

        res = []

        for _ in range(k):
            p = heapq.heappop(min_heap) #O(logN)
            res.append(p[1])

        return res
