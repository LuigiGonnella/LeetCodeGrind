# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#recursive leaf insertion
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

#         def insert(r):

#             if not r:
#                 return TreeNode(val)
            
#             if val < r.val:
#                 r.left = insert(r.left)
#             else:
#                 r.right = insert(r.right)
            
#             return r
        
        
#         return insert(root)

#iterative leaf insertion
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        cur = root

        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left




#root insertion
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(r):

            def rotR(ro):
                newH = ro.left
                ro.left = newH.right
                newH.right = ro

                return newH
            
            def rotL(ro):
                newH = ro.right
                ro.right = newH.left
                newH.left = ro
                return newH

            if not r:
                return TreeNode(val)
            
            if val < r.val:
                r.left = insert(r.left)
                r = rotR(r)
            else:
                r.right = insert(r.right)
                r = rotL(r)
            
            return r
        
        
        return insert(root)


        