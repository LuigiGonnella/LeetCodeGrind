class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        source = n

        for i in range(n): #n excluded but included in source already
            source ^= i ^ nums[i]
    
        return source
        