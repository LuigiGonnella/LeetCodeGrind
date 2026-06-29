
#!O(N ^ 3) time and O(N) space
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        occ = defaultdict(int)

        for num in nums:
            occ[num] += 1

        nums.sort()

        res = []
        for i in range(n):

            occ[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                occ[nums[j]] -= 1

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                for k in range(j + 1, n):
                    occ[nums[k]] -= 1

                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                
                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if occ[fourth]:
                        res.append([nums[i], nums[j], nums[k], fourth])
                
                for k in range(j + 1, len(nums)):
                    occ[nums[k]] += 1

            for j in range(i + 1, len(nums)):
                occ[nums[j]] += 1
        
        return res






        