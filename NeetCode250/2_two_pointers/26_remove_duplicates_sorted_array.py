class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 0 or n == 1:
            return n
        
        i, j = 0, 1

        while j < n:

            while j < n and nums[i] == nums[j]: #move j to first non-equal to nums[i] eleemnt
                j += 1
            
            i += 1 #in i + 1 i have to insert that first non-equal to nums[i] element, which is in nums[j]

            if i < n and j < n:
                nums[i] = nums[j]
        
        return i #the last eleemnt will be in i - 1 (since i always do i += 1 before inserting the element, so the last update will go out of bounds of k)

        