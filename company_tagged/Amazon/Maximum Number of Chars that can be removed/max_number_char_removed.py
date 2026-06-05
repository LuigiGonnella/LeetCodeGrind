
#!TWO POINTERS
#!O(N) time and O(1) space
class Solution:
    def solve(self, machine):
        start = machine[0]
        end = machine[-1]
        n = len(machine)


        if start == end:
            return n - 1
        
        dist = n #number of maintained elements 
        last_start = -1

        for r in range(n):

            if machine[r] == start:
                last_start = r

            if machine[r] == end and last_start != -1:
                curr_dist = r - last_start + 1 #chars maintained in this range
                if curr_dist < dist: #i want the fewest maintained
                    dist = curr_dist

        
        return n - dist 





        
