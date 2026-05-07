
#!COMBINATIONS LIKE O(4 ^ N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {}
        curr_idx = 0
        for i in range(8):
            num = i + 2
            chars[str(num)] = []
            k = 3 if num != 7 and num != 9 else 4

            for _ in range(k):
                chars[str(num)].append(chr(ord('a') + curr_idx))
                curr_idx += 1
            
                

        res = []
        curr = []
        def dfs(start: int):
            
            if len(curr) == len(digits):
                if curr:
                    res.append("".join(curr))
                return
            

            for i in range(start, len(digits)):
                for j in range(len(chars[str(digits[i])])):
                    curr.append(chars[str(digits[i])][j])
                    dfs(i + 1)
                    curr.pop()
        
        dfs(0)
        return res
                 
#!CLEAN O(4 ^ N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
                

        res = []
        curr = []
        def dfs(i: int):
            
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            

            for ch in chars[digits[i]]:
                curr.append(ch)
                dfs(i + 1)
                curr.pop()
        
        dfs(0)
        return res
        