
#!O(N * 2 ^ N) time and O(N + (M*T)) space con N =len(s) e T = maximum length of strings in dict
#same solution of palindromic substrings
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict) #O(1) lookups, O(M*T) space

        def dfs(i): #O(N) space for stack
            if i == n:
                return True
            
            for j in range(i, n):
                if s[i: j + 1] in wordSet and dfs(j + 1): #slice O(N)
                    return True
            
            return False
        
        return dfs(0)


#!O((N * T^2) + M) time and O(N + M * T) space con M = len(wordDict)
#MEMOIZATION
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        maxL = max([len(word) for word in wordDict]) #!O(M)

        wordSet = set(wordDict) #O(1) lookups
        memo = [-1] * n

        def dfs(i): #!DFS runnata massimo N volte
            if i == n:
                return True
            
            if memo[i] != -1:
                return memo[i]
            
            for j in range(i, min(n, i + maxL)): #!per ognuna --> ciclo T volte
                if s[i: j + 1] in wordSet and dfs(j + 1): #!slice con costo massimo T
                    memo[i] = True
                    return memo[i]
            
            memo[i] = False
            return memo[i]
        
        return dfs(0)

#!O((N * M * T) time and O(N) space
#BOTTOMP-UP (posso fare lo stesso con TRIE per cercare matches 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1) #is it possible to match from "i" to end?
        dp[n] = True #for empty string it is always True (nothing to match)

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                l = len(word)
                if word == s[i : i + l]:
                    dp[i] = dp[i + l]

                    if dp[i]:
                        break
        
        return dp[0]


#!O((N * T^2) + M) time and O(N + M * T) space, better if big M
#BOTTOM-UP, TRIE
class NodeTrie:
        def __init__(self):
            self.children = {}
            self.end = False

class Trie:
    def __init__(self):
        self.root = NodeTrie()
    
    def add(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = NodeTrie()
            curr = curr.children[char]
        
        curr.end = True
    
    def search(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.end

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        trie = Trie()

        maxL = -1
        for word in wordDict: #O(M)
            trie.add(word) #O(T)
            maxL = max(maxL, len(word))

        for i in range(n - 1, -1 , -1): #O(N)
            l = min(n, i + maxL)
            for j in range(i, l): #O(T)
                if trie.search(s[i: j + 1]): #O(T) #if in j ends an existent word
                    dp[i] = dp[j + 1]

                    if dp[i]:
                        break
        
        return dp[0]


           


        