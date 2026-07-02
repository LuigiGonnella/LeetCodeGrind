
#!0(logN) time and O(1) space
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()

        l, r = 0, len(nums)
        res = len(nums)
        
        while l < r:

            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
                res = m
        
        return res 