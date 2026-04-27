# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#!RECURSIVE DFS --> O(N * M) time and O(N + M) space
# class Solution:  
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            
            if not root or not subRoot or root.val != subRoot.val:
                return False
            
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#!SERIALIZATION + PATTERN MATCHING --> O(N + M) time and O(N + M) space
class Solution:  
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def z_function(self, s: str) -> list:
        z = [0] * len(s)

        l, r, n = 0, 0, len(s)

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_s = self.serialize(root)
        subRoot_s = self.serialize(subRoot)
        combined = subRoot_s + "|" + root_s

        z_values = self.z_function(combined)
        len_sub = len(subRoot_s)
        for i in range(len_sub + 1, len(combined)):
            if z_values[i] == len_sub:
                return True
        
        return False
        


        
        

