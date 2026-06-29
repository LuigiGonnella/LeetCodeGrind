
#!O(N) time and O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #we move in a cycle and if the steps don't cover all elements (n and k have a common divisor)
        #we start from next starting position

        n = len(nums)
        k = k % n

        count = start = 0

        while count < n:
            prev = nums[start]
            current = start

            while True:

                next_idx = (current + k) % n
                prev, nums[next_idx] = nums[next_idx], prev
                current = next_idx
                count += 1

                if current == start:
                    break
            
            start += 1