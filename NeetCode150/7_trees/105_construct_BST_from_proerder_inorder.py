# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#!RECURSIVE DFS WITH HASH MAP
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_mp = {}

        for i in range(len(inorder)):
            inorder_mp[inorder[i]] = i #says if already inserted in tree

        self.pre_id = 0        

        def dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            
            root_val = preorder[self.pre_id]
            self.pre_id += 1
            root = TreeNode(root_val)
            mid = inorder_mp[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        

        return dfs(0, len(inorder) - 1)

#!RECURSIVE DFS WITHOUT HASH MAP
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.in_id = 0
        self.pre_id = 0

        def dfs(limit: int) -> Optional[TreeNode]: #limit rappresenta lal boundary su cui fermarci
        #quando iteriamo su inorder da SX a DX.
        #questa boundary rappresenta il val del root da cui si va a SX. Infatti a SX di VAL in inorder ci sono tutti i vals del left subtree.
        #poi, andando a destra, continuiamo a prendere valori fintanto che rimaniamo PRIMA del val di root (right dei figli di root ddevono rimanere a sinistra del val di root)
            if self.pre_id >= len(preorder): #esaurito i nodi
                return None
            
            if inorder[self.in_id] == limit: #popolato sottoalbero sinistro (continuo ad aggiungere nodi nell'ordine preorder finche nell'inorder incontro root --> non devo piu aggiungere a SX ma a DX)
                self.in_id += 1
                return None
            
            root = TreeNode(preorder[self.pre_id])
            self.pre_id += 1

            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root
        
        return dfs(float("+inf"))

#!MORRIS TRAVERSAL
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right) #in later iterations this will be the start of the right subtree
            #since the left subtree will be completed
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]: #metto tutti a sx finche non incontro "boundary"
                curr.left = TreeNode(preorder[i], right=curr) #aggiungo pointer al padre
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]: #rimuovo pointers al padre
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

            #terminato il left, sono di nuovo al sono al padre originario, pronto per buildare il right
        return head.right
