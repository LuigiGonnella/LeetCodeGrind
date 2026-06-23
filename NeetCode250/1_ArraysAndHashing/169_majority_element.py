
#!O(N) time and space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = defaultdict(int)
        n = len(nums)

        for num in nums:
            occ[num] += 1
            if occ[num] > n // 2:
                return num

#!O(NlogN) time and O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums) // 2] #smallest eleemnt cannot be repeated until n // 2 so middle element is always the one who compares at least n // 2 times