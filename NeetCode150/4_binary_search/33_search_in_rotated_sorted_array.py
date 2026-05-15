class Solution:
    def _searchRotations(self, nums: List[int]) -> int: #equal to find the index of the minimum element
        l = 0
        r = len(nums) - 1
        minId = 0

        while l <= r:
            if nums[l] <= nums[r]:
                minId = l if nums[l] < nums[minId] else minId 
                return minId

            m = l + (r-l)//2
            minId = m if nums[m] < nums[minId] else minId 

            if nums[l] <= nums[m]: #already sorted, go right
                l = m + 1
            else: #not sorted, go left
                r = m - 1
        
        return minId
    
    def _searchR(self, nums: List[int], target: int, nRot: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m_sorted = l + (r-l)//2
            m_not_sorted = (m_sorted + nRot) % len(nums)

            if target == nums[m_not_sorted]:
                return m_not_sorted

            if target < nums[m_not_sorted]:
                r = m_sorted - 1
            else:
                l = m_sorted + 1
        
        return -1



    def search(self, nums: List[int], target: int) -> int:
        nRot = self._searchRotations(nums)

        return self._searchR(nums, target, nRot)


#OR, ONE SINGLE PASS:
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             mid = (l + r) // 2
#             if target == nums[mid]:
#                 return mid

#             if nums[l] <= nums[mid]:
#                 if target > nums[mid] or target < nums[l]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1

#             else:
#                 if target < nums[mid] or target > nums[r]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1



        