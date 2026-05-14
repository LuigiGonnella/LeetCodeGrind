
#O(1) in both space and time
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res += 1 if n & 1 else 0
            n >>= 1
        return res

#OPTIMIZATION --> skip zeros without checking
# IF WE DO n – 1 we flip the LEST SIGNIFICANT 1 to 0 and TRANSFORM ALL THE ZEROS TO ITS RIGHT TO ONES (if any)
# IF WE DO n & (n – 1) we TRANSFORM TO 0 the LEAST SIGNIFICANT ONE present in n skipping iterating over the leading ZEROS
# I CAN CONTINUE UNTIL N IS 0

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1) #skip zeros
            res += 1
        return res

        