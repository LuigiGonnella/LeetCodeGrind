# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#rotation based deletion --> bring node to leaf and delete leaf
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete(r):

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
                return None

            if key < r.val:
                r.left = delete(r.left)
            
            elif key > r.val:
                r.right = delete(r.right)
            
            else:
                if not r.right and not r.left:
                    return None

                if r.left:
                    r = rotR(r)
                    r.right = delete(r.right)
                elif r.right:
                    r = rotL(r)
                    r.left = delete(r.left)

            
            return r
        
        return delete(root)

#standard deletion --> if only 1 child: replace node with childe. If 2 children --> find successor, replace value and delete successor
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:

            if not root.left or not root.right:
                return root.left if root.left else root.right 
            else:

                successor = root.right

                while successor.left:
                    successor = successor.left
                
                root.val = successor.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root


            


        