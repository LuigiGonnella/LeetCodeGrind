class Solution:
    def solve(self, host_throurghput):
        
        n = len(host_throurghput)
        host_throurghput.sort() #NlogN

        l = 0
        r = n - 1
        throughput = 0

        while l <= r - 2:

            throughput += host_throurghput[r - 1]
            l += 1
            r -= 2
        
        return throughput

