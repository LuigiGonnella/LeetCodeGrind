
#!O(N ^ 2)
class Solution:
    def solve(self, power) -> int:
        mod = 1000000007
        n = len(power)
        res = 0

        for k in range(1, n + 1): #O(N)
            q = deque()
            running_sum = 0
            for idx in range(n): #o(N)
                running_sum += power[idx]
                running_sum %= mod

                if idx >= k:
                    running_sum -= power[idx - k]

                #delete all indexes out of bounds
                while q and q[0] <= idx - k:
                    q.popleft()
                    
                
                #maintain the increasing property
                while q and power[q[-1]] >= power[idx]:
                    q.pop()
                
                q.append(idx) #add eleemnt to window
                

                if idx >= k - 1: #for each window
                    new_power = (power[q[0]] * running_sum) % mod
                    res += new_power
                    res %= mod

        return res


#!O(N)
class Solution:
    def solve(self, power: list[int]) -> int:
        MOD = 1000000007
        n = len(power)
        
        # 1. Build standard prefix sums (P)
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = (P[i] + power[i]) % MOD
            
        # 2. Build prefix sums of prefix sums (PP)
        PP = [0] * (n + 2)
        for i in range(n + 1):
            PP[i + 1] = (PP[i] + P[i]) % MOD
            
        # 3. Find next smaller element to the left
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and power[stack[-1]] >= power[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        # 4. Find next smaller element to the right
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and power[stack[-1]] > power[i]: # Strict inequality handles duplicates safely
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        # 5. Calculate total power across all windows
        total_power = 0
        for i in range(n):
            l_bound = left[i]
            r_bound = right[i]
            
            count_left = i - l_bound
            count_right = r_bound - i
            
            # Range sum of P from index i+1 to r_bound
            sum_P_right = (PP[r_bound + 1] - PP[i + 1]) % MOD
            # Range sum of P from index l_bound+1 to i
            sum_P_left = (PP[i + 1] - PP[l_bound + 1]) % MOD
            
            # Total subarray sums anchored by power[i]
            total_subarray_sum = (count_left * sum_P_right - count_right * sum_P_left) % MOD
            
            # Multiply by the minimum element itself
            current_contribution = (power[i] * total_subarray_sum) % MOD
            total_power = (total_power + current_contribution) % MOD
            
        return (total_power + MOD) % MOD