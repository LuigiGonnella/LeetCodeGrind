# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

#         res = []

#         def dfs(r):
#             nonlocal res

#             if not r:
#                 return
            
#             dfs(r.left)
#             dfs(r.right)
#             res.append(r.val)


#         dfs(root)
#         return res  

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left

        res.reverse()
        return res
                

        