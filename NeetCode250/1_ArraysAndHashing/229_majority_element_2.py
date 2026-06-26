
#!FREQUENCY MAP: O(N) time and space

#!O(NlogN) and O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        curr = nums[0]
        rep = 1

        n = len(nums)
        res = []
        for num in nums[1:]:
            if rep > n // 3:
                if not res or (res and res[-1] != curr):
                    res.append(curr)

            if num == curr:
                rep += 1
            else:
                curr = num
                rep = 1
        
        if rep > n // 3:
            if not res or (res and res[-1] != curr):
                res.append(curr)
        
        return res


#!Boyer-Moore --> O(N) and O(1) space (map capped at 2)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            tmp = defaultdict(int)
            for el in count:
                if count[el] > 1:
                    tmp[el] = count[el] - 1
            
            count = tmp
 
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3: #another pass on nums to check actual count of survivors in count (not assured to have frequency > n // 3 yet)
                res.append(num)
        
        return res


 