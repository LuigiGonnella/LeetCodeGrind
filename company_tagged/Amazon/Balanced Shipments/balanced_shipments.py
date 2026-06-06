class Solution:
    def solve(self, weights) -> int:
        n = len(weights)

        dp = [-1] * (n + 1) #maximum number of segments if the BOUNDARY WAS i
        #e.g. [1, 2, 3] --> dp[3] = -1 since we cannot set a boundary here (no bigger elements to left)
        dp[0] = 0 #null list


        #e.g. [1, 2, 3] --> max_dp[3] = 0 since we we can nevere set a boundary even on other elements on the left --> 0 maximum segments
        max_dp = [-1] * (n + 1) #prefix max of dp --> maximum number of segments WHEREVER up to i

        stack = [] #monotonic stack to get first element on the left BIGGER than current

        for i in range(1, n + 1):

            while stack and weights[stack[-1]] <= weights[i - 1]:
                stack.pop()
            
            if stack: #top is first bigger than current
                k = stack[-1]

                if max_dp[k] != -1: #we already found best shipment for k
                    dp[i] = max_dp[k] + 1 #we add one shipment
            
            stack.append(i)
            max_dp[i] = max(max_dp[i - 1], dp[i])

        return max(0, dp[n])
    
    #dato che la soluzione che ci interessa e solo in dp[n] --> TAGLIO FORZATO ALLA FINE (dobbiamo FINIRE avendo un taglio valido come last element) --> ritorniamo dp[n]
    #inoltre max_dp memorizza solo lo STORICO --> BEST POSSIBLE NUMBER OF SEGMENTS FINO A i ma POSSIBILMENTE ESCLUDENDO ALCUNI VALORI PRIMA DI i (tiene in memoria il best maximum number of segments invcontrati fino a i a prescindere da dove sono avvenuti i tagli)
        