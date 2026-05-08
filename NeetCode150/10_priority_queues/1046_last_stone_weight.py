class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        #!O(NlogN)
        while len(max_heap) > 1: #O(N)
            diff = heapq.heappop(max_heap) - heapq.heappop(max_heap)
            if diff:
                heapq.heappush(max_heap, diff) #O(logN)

        return -max_heap[0] if max_heap else 0
        