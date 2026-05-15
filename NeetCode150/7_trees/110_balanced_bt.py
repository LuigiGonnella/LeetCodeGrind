# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!RECURSIVE DFS, O(N) time, O(N) space
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root: Optional[TreeNode]) -> int:
            if not root or not self.balanced:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return 1 + max(left, right)
        
        _ = dfs(root)

        return self.balanced

#!ITERATIVE DFS, O(N) time, O(N) space
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [root]
        nd = {None : 0}

        while stack:
            node = stack[-1]

            if node.left and node.left not in nd:
                stack.append(node.left)
            elif node.right and node.right not in nd:
                stack.append(node.right)
            else:
                node = stack.pop()
                lh = nd[node.left]
                rh = nd[node.right]

                if abs(lh - rh) > 1:
                    return False

                nd[node] = 1 + max(lh, rh)
        
        return True






