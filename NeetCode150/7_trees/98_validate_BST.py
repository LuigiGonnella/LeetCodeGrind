# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!RECURSIVE DFS --> O(N) time and O(N) space
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True


        def dfs(root: Optional[TreeNode], lastPL: int, lastPR: int) -> bool:
            if not root:
                return True
            
            if root.val <= lastPL or root.val >= lastPR:
                return False
            
            return dfs(root.left, lastPL, root.val) and dfs(root.right, root.val, lastPR)
            
        
        return dfs(root, float("-inf"), float("+inf"))

#!ITERATIVE BFS --> O(N) time and O(N) space
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        queue = deque([(root, float("-inf"), float("+inf"))])
        
        while queue:
            node, maxPL, minPR = queue.popleft()

            if node.val <= maxPL or node.val >= minPR:
                return False
            
            if node.left:
                queue.append((node.left, maxPL, node.val))
            
            if node.right:
                queue.append((node.right, node.val, minPR))
        
        return True
        
        
        