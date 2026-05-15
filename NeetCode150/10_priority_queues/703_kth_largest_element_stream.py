
class KthLargest:
    #!O(logN) heapify
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        #remove until len == k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        
    #!O(m * logK) with m = numbers of adds
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]