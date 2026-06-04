

#!O(N! * N)
#BRUTE FORCE
class Solution:

    def solve(self, data) -> List[int]:

        n = len(data)
        mark = [0] * n
        curr_sol = []
        self.res = []
        self.maxSum = float("-inf")
        
        def dfs():

            def update(curr_sol):
                tot = 0
                for i in range(n):
                    tot += (i + 1) * data[curr_sol[i] - 1]
                
                if tot > self.maxSum or (tot == self.maxSum and curr_sol < self.res):
                    self.maxSum = tot
                    self.res = curr_sol.copy()



            if len(curr_sol) == n:
                update(curr_sol)


            for i in range(n):
                if not mark[i]:
                    mark[i] = 1
                    curr_sol.append(i + 1)
                    dfs()
                    curr_sol.pop()
                    mark[i] = 0
        
        dfs()

        return self.res



class Solution:
    #Since it is a simple multiplication of data[i] * step and step is increasing, the biggest sum will be the one with SORTED DATA
    #So we only need to find the ored of indexes SORTING DATA
    #Tiebreaker is the value of the index
    def solve(self, data) -> List[int]:

        n = len(data)
        
        return sorted(range(1, n + 1), key =lambda x: (data[x - 1], x)) #small coefficients to small data, large coefficient to large data