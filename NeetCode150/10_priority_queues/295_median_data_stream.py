class MedianFinder:

    def __init__(self):
        self.min_heap = [] #greater half
        self.max_heap = [] #smallest half
     

    def addNum(self, num: int) -> None: #!O(logN)

        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, - val)


    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2 
        
        return self.min_heap[0] if len(self.min_heap) > len(self.max_heap) else  -self.max_heap[0]