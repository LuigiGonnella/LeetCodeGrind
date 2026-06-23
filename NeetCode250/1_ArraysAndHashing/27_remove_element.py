
#!TWO POINTERS --> !O(N) time O(1) space
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

#!O(NlogN) time O(1) space
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)
        start, end = -1, -1

        for i in range(n):
            if nums[i] == val and start == -1:
                start = i
            if nums[i] == val and start != -1:
                end = i
            if nums[i] != val and end != -1:
                break
        
        if start == -1:
            return n

  
        k = end - start + 1
        idx = n - 1
        while idx >= 0 and start < len(nums) and start < idx and nums[start] == val and nums[idx] != val:
            nums[start], nums[idx] = nums[idx], nums[start] 
            start += 1
            idx -= 1
        
        return n - k

#!O(N) time O(N) space
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)




        