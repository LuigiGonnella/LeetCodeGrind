
#!BST LIKE
class TreeNode:
    def __init__(self, val = "", left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class PrefixTree:

    def __init__(self):
        self.root = None
        

    def insert(self, word: str) -> None:
        if not self.root:
            self.root = TreeNode(word)
            return
        
        def insertR(curr: Optional[TreeNode], word: str) -> Optional[TreeNode]:
            if not curr:
                return TreeNode(word)
            
            if word < curr.val:
                curr.left = insertR(curr.left, word)
            elif word > curr.val:
                curr.right = insertR(curr.right, word)
     
            return curr

        insertR(self.root, word)


    def search(self, word: str) -> bool:
        if not self.root:
            return False
        
        def searchR(curr: Optional[TreeNode], word: str) -> bool:
            if not curr:
                return False
            
            if word == curr.val:
                return True
            if word < curr.val:
                return searchR(curr.left, word)

            return searchR(curr.right, word)
            
        
        return searchR(self.root, word)


    def startsWith(self, prefix: str) -> bool:
        if not self.root:
            return False
        
        def searchR(curr: Optional[TreeNode], word: str) -> bool:
            if not curr:
                return False
            

            if curr.val.startswith(word):
                return True
            elif word < curr.val:
                return searchR(curr.left, word)
            return searchR(curr.right, word)

        return searchR(self.root, prefix)

#!ARRAY
#!O(N) time and O(t) space (t = nukmber of different paths)
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.endOfWord = True

       


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            
            curr = curr.children[idx]

        return curr.endOfWord
        


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        
        return True
        


#!HASH MAP, same
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True




        
        







        
        