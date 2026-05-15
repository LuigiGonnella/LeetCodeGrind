# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!RECURSIVE DFS
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.finalsum = root.val

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return float("-inf")
            
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)

            biggest = leftsum if leftsum > rightsum else rightsum
            lowest =  rightsum if leftsum > rightsum else leftsum
            
            if lowest >= 0:  
                tot = biggest + lowest + root.val #currmax puo essere fatto da root + left + right
            elif biggest >= 0:
                tot = biggest + root.val
            else:
                tot = root.val

            if tot > self.finalsum:
                self.finalsum = tot
            #connect
            if biggest > 0:
                return biggest + root.val #ma propago solo biggest sum tra left + root, right + root, left + right + root, root

            return root.val
        
        dfs(root)

        return self.finalsum

#!CLEAN RECURSIVE DFS
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.finalsum = root.val

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)

            leftsum = max(0, leftsum)
            rightsum = max(0, rightsum)
            
            self.finalsum = max(self.finalsum, leftsum + rightsum + root.val)

            return root.val + max(leftsum, rightsum)
        
        dfs(root)

        return self.finalsum
            
            
            