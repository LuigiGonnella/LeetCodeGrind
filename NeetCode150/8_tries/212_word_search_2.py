
#!DFS
#O(W*R*C*4*3*(T-1)) time (3 because every time we mark a cell, in the next recursion level, we will NOT go back here)
# O (T) space (T = max length of any word)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n_rows = len(board)
        n_cols = len(board[0]) if board else 0

        res = []

        def dfs(r, c, idx, word) -> bool:
            if idx >= len(word):
                return True

            if r < 0 or r >= n_rows or c < 0 or c >= n_cols or word[idx] != board[r][c]:
                return False
            

            board[r][c] = "*" #mark

            inner = (dfs(r, c + 1, idx + 1, word) or
            dfs(r, c - 1, idx + 1, word) or
            dfs(r + 1, c, idx + 1, word) or
            dfs(r - 1, c, idx + 1, word))

            board[r][c] = word[idx] #backtrack

            return inner

        
        for word in words:
            flag = False
            for r in range(n_rows):
                if flag:
                    break
                for c in range(n_cols):
                    if board[r][c] != word[0]:
                        continue
                    if dfs(r, c, 0, word):
                        res.append(word)
                        flag = True
                        break
        
        return res


#!TRIE (hashmap) + DFS
#O(R*C*4*3^(T-1) + S) time (3 because every time we mark a cell, in the next recursion level, we will NOT go back here)
#O(S) space (S = sum of lengths all words)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        n_rows = len(board)
        n_cols = len(board[0]) if board else 0

        for word in words:
            trie.addWord(word)

        res = set()

        def dfs(r, c, node, word):
            if r < 0 or r >= n_rows or c < 0 or c >= n_cols or board[r][c] not in node.children:
                return 
            
            
            
            word += board[r][c]
            node = node.children[board[r][c]]

            tmp = board[r][c] 
            board[r][c] = "*" #mark

            if node.end:
                res.add(word) #set avoids duplicates

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            board[r][c] = tmp #backtrack
        
        for r in range(n_rows):
            for c in range(n_cols):
                dfs(r, c, trie.root, "")
        
        return list(res)


#!TRIE (array) + DFS + PRUNING 
# O(R*C*4*3^(T -1) + S) time (3 because every time we mark a cell, in the next recursion level, we will NOT go back here)
# O(S) space (S = sum of lengths all words)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.refs = 0
        self.idx = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word, i):
        curr = self.root
        curr.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            
            curr = curr.children[index]
            curr.refs += 1
        
        curr.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        n_rows = len(board)
        n_cols = len(board[0]) if board else 0

        for i, word in enumerate(words):
            trie.addWord(word, i)

        res = []

        def dfs(r, c, node):
             
            if r < 0 or r >= n_rows or c < 0 or c >= n_cols or board[r][c] == "*" or not node.children[ord(board[r][c]) - ord('a')]:
                return 
            
            index = ord(board[r][c]) - ord('a')
 
            tmp = board[r][c] 
            board[r][c] = "*" #mark
            prev = node
            node = node.children[index]

            if node.idx != -1:
                res.append(words[node.idx]) #set avoids duplicates
                node.refs -= 1
                node.idx = -1
                if node.refs == 0:
                    prev.children[index] = None #avoids future paths through this node
                    node = None
                    board[r][c] = tmp #backtrack
                    return

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = tmp #backtrack
        
        for r in range(n_rows):
            for c in range(n_cols):
                dfs(r, c, trie.root)
        
        return res




            
        