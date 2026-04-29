# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!RECURSIVE DFS --> O(h + k) time (h in depth + k in reverse) but O(N) worst case. O(N) space
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None

        def dfs(root: Optional[TreeNode], k: int) -> int:
            if not root or self.res:
                return 0
            
            l = dfs(root.left, k)

            if l + 1 == k:
                self.res = root.val

            r = dfs(root.right, k - l - 1)

            return l + r + 1


        dfs(root, k)
        return self.res
        

#!RECURSIVE DFS --> O(h + k) time (h in depth + k in reverse) but O(N) worst case. O(N) space
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = None

        def dfs(root: Optional[TreeNode]) -> None:
            if not root or self.res:
                return
            
            dfs(root.left) #search in left

            self.count -= 1
            if self.count == 0: #if k-th smallest
                self.res = root.val #return

            dfs(root.right) #go right

        dfs(root)

        return self.res

#!ITERATIVE DFS --> O(h + k) time (h in depth + k in reverse) but O(N) worst case. O(N) space
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:  
            while curr:
                    stack.append(curr)                   
                    curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right



#!MORRIS TRAVERSAL (inorder traversal with O(1) space)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        while curr:
            if not curr.left: #smallest --> valuto
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right #continuo ricerca a destra (vero destro o SUCCESSORE)
            else:
                pred = curr.left
                while pred.right and pred.right != curr: #trovo PREDECESSORE
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else: #qui entro quando sto risalendo --> valuto in risalita ogni nodo CURR
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        return -1
                









            


        