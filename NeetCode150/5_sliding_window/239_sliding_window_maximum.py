
#MAX HEAP --> O(NlogN)
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         heap = []
#         output = []

#         for i in range(len(nums)):
#             heapq.heappush(heap, (-nums[i], i))

#             if i >= k - 1:
#                 while heap[0][1] < (i - k + 1):
#                     heapq.heappop(heap)
                
#                 output.append(-heap[0][0])

#         return output

#DEQUE --> O(N)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m_deque = deque([])
        output = []

        for r in range(len(nums)):    
            while m_deque and nums[r] > nums[m_deque[-1]]:
                m_deque.pop()

            m_deque.append(r)
        
            if m_deque[0] <= r - k:
                m_deque.popleft()

            if r >= k - 1:
                output.append(nums[m_deque[0]])

            


        return output

