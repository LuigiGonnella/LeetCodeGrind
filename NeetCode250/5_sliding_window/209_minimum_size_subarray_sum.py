
#!O(N) time and O(1) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        l = 0
        tot = nums[0]
        minLen = float("+inf")

        for r in range(1, n):

            while tot >= target and l < r:
                minLen = min(minLen, r - l)
                tot -= nums[l]
                l += 1
            
            tot += nums[r]
            
        
        while tot >= target and l < n:
            minLen = min(minLen, n - l)
            tot -= nums[l]
            l += 1

        return minLen if minLen != float("+inf") else 0


#!O(NlogN) time and O(1) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        minLen = float("+inf")

        for i in range(n): #i will be the start index
            l, r = i, n - 1 #binary search between i and n - 1 to find end index

            while l <= r:

                m = l + (r - l) // 2
                currSum = prefix[m + 1] - prefix[i]

                if currSum >= target:
                    minLen = min(minLen, m - i + 1)
                    r = m - 1
                else:
                    l = m + 1
        
        return minLen if minLen != float("+inf") else 0




