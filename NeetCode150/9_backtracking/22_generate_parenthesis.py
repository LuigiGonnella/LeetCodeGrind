
#!BRUTE FORCE --> PERMUTATIONS with repetitions --> O((2N!)/ (N! * N!)) = O(binomial of 2n on n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        candidates = ["(", ")"]        
        occ = {"(": n, ")": n}


        def check(candidates: List[int]) -> bool:
            open_sum = 0
            closed_sum = 0

            for p in candidates:
                open_sum += 1 if p == "(" else 0
                closed_sum += 1 if p == ")" else 0

                if closed_sum > open_sum:
                    return False
            
            return True

        def dfs() -> None:
            if len(curr) == 2*n:
                if check(curr):
                    res.append("".join(curr))
                return
            
            for i in range(len(candidates)):    
                if occ[candidates[i]] > 0:
                    occ[candidates[i]] -= 1
                    curr.append(candidates[i])

                    dfs()

                    curr.pop()
                    occ[candidates[i]] += 1

                    

        dfs()
        return res


#!PRUNING --> PERMUTATIONS with repetitions --> O((binomial of 2n on n) divided by (n + 1)) = catalan number = 4^N / (N ^ (3/2))
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        candidates = ["(", ")"]        
        occ = {"(": n, ")": n}


        def dfs(open_sum, closed_sum) -> None:
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
            
            for i in range(len(candidates)):    
                el = candidates[i] 
                if occ[el] > 0:
                    if el == "(":
                        occ[el] -= 1
                        curr.append(el)

                        dfs(open_sum + 1, closed_sum)

                        curr.pop()
                        occ[el] += 1
                    elif open_sum >= closed_sum + 1:
                        occ[el] -= 1
                        curr.append(el)

                        dfs(open_sum, closed_sum + 1)

                        curr.pop()
                        occ[el] += 1

        dfs(0, 0)
        return res



#! DP (same complexity)
class Solution:
    def generateParenthesis(self, n):
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)

        return res[-1]