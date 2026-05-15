"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#!O(N) time with 1 PASS and O(N) space (3*N considering stack + map + output list)
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        occMap = {}

        def copyR(head: Optional[Node]) -> Optional[Node]:
            if head is None:
                return None
            if head in occMap:
                return occMap[head]

            newHead = Node(head.val, None, None)
            occMap[head] = newHead
            newHead.next = copyR(head.next)
            newHead.random = copyR(head.random)

            return newHead

        return copyR(head)
    
#!O(N) time with 2 PASS and O(N) space (2*N considering map + output list)
# class Solution:
#     def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
#         if head is None:
#             return None

#         occMap = {}

#         curr = head
#         while curr:
#             occMap[curr] = Node(curr.val)
#             curr = curr.next
        
#         curr = head
#         newHead = occMap[head]
#         while curr:
#             if curr.next:
#                 occMap[curr].next = occMap[curr.next]
#             else:
#                 occMap[curr].next = None
#             if curr.random:
#                 occMap[curr].random = occMap[curr.random]
#             else:
#                 occMap[curr].random = None
            
#             curr = curr.next
            
#         return newHead

#!O(N) time with 1 PASS and O(N) space (2*N considering map + output list)
# class Solution:
#     def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

#         occMap = defaultdict(lambda: Node(0))
#         occMap[None] = None

#         curr = head
#         while curr:
#             occMap[curr].val = curr.val
#             occMap[curr].next = occMap[curr.next]
#             occMap[curr].random = occMap[curr.random]
#             curr = curr.next
        
#         return occMap[head]

#!O(N) time with 3 PASS and O(1) extra space (N considering output list)
# class Solution:
#     def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
#         if head is None:
#             return None

#         curr = head
#         while curr:
#             curr.next = Node(curr.val, curr.next, None)
#             curr = curr.next.next
        
#         curr = head
#         while curr:
#             curr.next.random = curr.random.next if curr.random else None
#             curr = curr.next.next
        
#         newHead = head.next

#         prev = head
#         curr = head.next
#         while curr:
#             tmp1 = prev.next.next
#             tmp2 = curr.next.next if curr.next else None
#             prev.next = curr.next
#             curr.next = curr.next.next if curr.next else None

#             prev = tmp1
#             curr = tmp2
        
#         return newHead


















        