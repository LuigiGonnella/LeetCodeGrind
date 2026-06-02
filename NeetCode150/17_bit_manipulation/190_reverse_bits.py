
#!O(1) time and space
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            res |= (bit << (31 - i))
          
        
        return res
        