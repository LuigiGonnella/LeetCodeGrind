#BRUTE-FORCE
#!O(N^2) time and O(1) space
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        for curr_start in range(n):
            curr_amount = gas[curr_start]
            curr_cost = cost[curr_start]

            j = curr_start

            while curr_amount >= curr_cost:
                j = (j + 1) % n

                if j == curr_start:
                    return curr_start
                
                curr_amount -= curr_cost
                curr_amount += gas[j]
                curr_cost = cost[j]
        
        return -1

#GREEDY --> scan mataining curr_diff, and if it goes negative --> start from next who can fill this negative number
#!O(N) time and O(1) space
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        curr_start = n - 1
        cumu_gain = 0
        curr_end = curr_start
        tot_diff = 0
        
        while curr_start >= 0:
            curr_amount = gas[curr_start]
            curr_cost = cost[curr_start]

            cumu_gain += (curr_amount - curr_cost)                 

            if cumu_gain + tot_diff < 0:
                curr_start -= 1
                continue
            
            tot_diff += cumu_gain 

            while tot_diff >= 0:
                curr_end = (curr_end + 1) % n

                if curr_start == curr_end:
                    return curr_start

                tot_diff += (gas[curr_end] - cost[curr_end])

            cumu_gain = 0
            curr_start -= 1

        return -1
        
#GREEDY CLEAN
#!O(N) time and O(1) space
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)

        res = 0
        total = 0

        for i in range(n):
            total += (gas[i] - cost[i])

            if total < 0: #impossible to start from 0 to i
                res = i + 1
                total = 0
        
        return res


