#!ITERATIVE BFS --> better for shortest path or 'closest match'
#time O(26 ^ N)
#space O(26 ^ N)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.endWord = True
        
 
    def search(self, word: str) -> bool:
        queue = deque([self.root])
        idx = 0

        while queue and idx < len(word):
            found = False
            for _ in range(len(queue)):
                curr = queue.popleft()

                if word[idx] == ".":
                    found = True
                    for key in list(curr.children.keys()):
                        queue.append(curr.children[key]) 

                elif word[idx] in curr.children:
                    queue.append(curr.children[word[idx]])
                    found = True
            
            if not found:
                return False
                
            idx += 1
        
        while queue:
            el = queue.popleft()
            if el.endWord:
                return True
        
        return False
            
#!RECURSIVE DFS --> better searching any solution
#time O(26 ^ N)
#space O(N)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.endWord = True
        
 
    def search(self, word: str) -> bool:

        def dfs(node: TrieNode, idx: int) -> bool:
            curr = node

            for i in range(idx, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    
                    return False     
                else:
                    if c not in curr.children:
                        return False
                    
                    curr = curr.children[c]
            
            return curr.endWord
        
        return dfs(self.root, 0)

        
            




        




        
