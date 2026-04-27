# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#O(N^2) time, O(N) space
# class Solution:
#     def getHeight(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         lh = self.getHeight(root.left)
#         rh = self.getHeight(root.right)

#         if lh > rh:
#             return lh + 1
        
#         return rh + 1


#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         currSol = self.getHeight(root.left) + self.getHeight(root.right)
#         lSol = self.diameterOfBinaryTree(root.left)
#         rSol = self.diameterOfBinaryTree(root.right)

#         if lSol > currSol:
#             currSol = lSol
        
#         return max(currSol, rSol)

#RECURSIVE DFS --> O(N) time, O(N) space
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.diameter = 0

#         def dfs(root: Optional[TreeNode]) -> int:
#             if not root:
#                 return 0
            
#             left = dfs(root.left)
#             right = dfs(root.right)
#             self.diameter = max(self.diameter, left + right) #DIAMETER AT THIS NODE = sum maximum heights of left and right children

#             return 1 + max(left, right) #return height at current node
        
#         _ = dfs(root)
#         return self.diameter


#ITERATIVE DFS -->O(N) time, O(N) space
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: #tracks the best diameter in each subtree (best diamter is the best in the root)
        if not root:
            return 0
        
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1] #don't pop it since we want POST ORDER (L, R, root) visit
            
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                currHeight = 1 + max(mp[node.left][0], mp[node.right][0])
                currDiameter = max(mp[node.left][1], mp[node.right][1], mp[node.right][0] + mp[node.left][0])

                mp[node] = (currHeight, currDiameter)
                

        return mp[root][1]







        
        