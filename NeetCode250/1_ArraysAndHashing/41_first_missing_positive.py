#!O(maxEl) time and O(1) space
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         maxEl = max(nums)
#         mask = 0
#         for num in nums:
#             if num > 0:
#                 mask |= 1 << num
        
#         for num in range(1, maxEl + 1):
#             if not (mask >> num) & 1:
#                 return num
        
#         return maxEl + 1 if maxEl > 0 else 1


#!O(N) time and O(1) space
#since positives starts from 1, in my array I can have from 1 up to len(nums) as value of a single entry
#so i can mark, for each positive number, its presence by marking the number in the index abs(number) - 1 as its value but negative, so also for that value i will not 
#change its abs value and i can evaluate it
# for negative number put them to 0 initially and skip them while processing abs values
#same for numbers > n
#if a number in nums[abs(num) - 1] was already zero, to mark it as negative, we mark as -(n + 1) so when we evaluate it we will skip it
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            val = abs(num)

            if val >= 1 and val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = - (n + 1)
            
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i
        
        return n + 1
                