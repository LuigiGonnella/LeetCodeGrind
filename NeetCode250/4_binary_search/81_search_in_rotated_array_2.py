
#!O(logN) but O(N) worst case (l += 1 in nums[l] == nums[m] scenario)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            
            if nums[l] < nums[m]: #left side is sorted

                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] > nums[m]: #right side is sorted

                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else: # increment and try again
                l += 1
        
        return False
        