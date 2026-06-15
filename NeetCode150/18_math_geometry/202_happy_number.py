
#!O(logn) time and O(logn) space
class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True

        def getNext(num):
            tot = 0
            while num > 0:
                tot += (num % 10) ** 2
                num //= 10
            
            return tot
        
        seen = set()

        while True:

            nextEl = getNext(n)
        
            if nextEl == 1:
                return True
            
            if nextEl in seen:
                return False
            
            seen.add(nextEl)
            n = nextEl

#!O(logn) time and O(1) space
class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True

         
        def getNext(num):
            tot = 0
            while num > 0:
                tot += (num % 10) ** 2
                num //= 10
            
            return tot
        
        slow, fast = n, getNext(n)

        while slow != fast:

            fast = getNext(getNext(fast))
            slow = getNext(slow)
        
        return True if fast == 1 else False