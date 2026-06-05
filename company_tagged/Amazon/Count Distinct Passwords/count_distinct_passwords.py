
#!BRUTE FORCE --> O(N ^ 3) --> track every substring, add to a set the resulting string --> if a substring geenrates a new password --> add


#OPTIMAL SOLUTION
#!O(N)
class Solution:
    def solve(self, password):

        n  = len(password)

        disitnct_pairs = n * (n - 1) // 2

        counter = Counter(password)

        for k in counter:
            equal_pairs = k * (k - 1) // 2

            disitnct_pairs -= equal_pairs
        
        return disitnct_pairs + 1 #the original password
