#! O(N) space
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         uniques = set()

#         for num in nums:
#             if num in uniques:
#                 return num
#             uniques.add(num)
        
#         return int("-inf")

#NEGATIVE NUMBERS
#! O(1) space
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         for num in nums:
#             idx = abs(num) - 1
#             if nums[idx] < 0:
#                 return abs(num)
#             nums[idx] *= -1
        
#         return -1

#BINARY SEARCH
#! O(1) space but O(NlogN) time
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         l, r = 1, len(nums) - 1

#         while l < r:
#             m = l + (r - l) // 2

#             uniques = sum(1 if num <= m else 0 for num in nums)

#             if uniques <= m:
#                 l = m + 1
#             else:
#                 r = m 
        
#         return l

# BIT MANIPULATION
# ! O(1) space and O(N) time (32 passes)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         res = 0
#         n = len(nums)

#         for b in range(32):
#             x, y = 0, 0
#             mask = 1 << b

#             for num in nums:
#                 if num & mask:
#                     x += 1
#             for num in range(1, n):
#                 if num & mask:
#                     y += 1

#             if x > y:
#                 res |= mask
        
#         return res

# BIT MANIPULATION
# ! O(1) space and O(N) time (32 passes)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow




















