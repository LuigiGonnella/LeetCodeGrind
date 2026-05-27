
#!BRUTE FORCE O(N^2) time and O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = float("-inf")
        for start in range(n):
            currSum = 0
            for j in range(start, n):
                currSum += nums[j]
                maxSum = max(maxSum, currSum) #important to update every time --> every j can be end --> in this way we evaluate all possible subarrays

        return maxSum




#!O(n) time and O(1) space
#KADANE'S ALGORITHM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        
        return max_sum
        