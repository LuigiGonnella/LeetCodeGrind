
#!O(KlogN)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]

        heapq.heapify(max_heap)


        for _ in range(k - 1):
            heapq.heappop(max_heap)
        
        return - heapq.heappop(max_heap)


#!O(NlogK)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [num for num in nums[:k]]

        heapq.heapify(min_heap)


        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        return min_heap[0]   

#!QuickSelect O(N^2) but O(N) average
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k #first ke lowest element --> Kth is the Kth largest

        def quickSelect(l, r):

            def partition():
                pivot = nums[r]
                i = l - 1
                j = r 

                while True:

                    while True:
                        i+=1
                        if nums[i] >= pivot:
                            break
                 
                    while True:
                        j-=1
                        if nums[j] <= pivot:
                            break

                    if i >= j:
                        break
                    
                    nums[i], nums[j] = nums[j], nums[i]

                nums[i], nums[r] = nums[r], nums[i]
                return i 

            q = partition()

            if q > k:
                return quickSelect(l, q - 1)
            elif q < k:
                return quickSelect(q + 1, r)
            else:
                return nums[q]
        
        return quickSelect(0, len(nums) - 1)

            














