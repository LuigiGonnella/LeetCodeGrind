# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#SINGLE PASS: O(N) time and O(1) space
class Solution: 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        prev = None

        while n > 0:
            n-=1
            right = right.next
        
        while right:
            prev = left
            left = left.next
            right = right.next
        
        if prev:
            prev.next = left.next
            
        else:
            head = head.next
        
        
        return head

#DUMMY NODE SOLUTION
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
#         left = dummy
#         right = head

#         while n > 0:
#             right = right.next
#             n -= 1

#         while right:
#             left = left.next
#             right = right.next

#         left.next = left.next.next
#         return dummy.next
        


#SEVERAL PASSES: O(N) time and O(1) space
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

#         def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#             y = head
#             revHead = None

#             while y:
#                 t = y.next
#                 y.next = revHead
#                 revHead = y

#                 y = t
            
#             return revHead
        
#         revHead = reverseList(head)

        
#         if n == 1 and revHead.next is None:
#             revHead = None
#         elif n == 1:
#             revHead = revHead.next
#         else:
#             prev = revHead
#             curr = revHead.next
#             for _ in range(n - 2):
#                 prev = curr
#                 curr = curr.next

#             prev.next = curr.next
        
#         return reverseList(revHead)
        

#RECURSION: O(N) time and O(N) space
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if n == 1 and head.next is None:
#             return None

#         def removeR(prev: Optional[ListNode], curr: Optional[ListNode], n: int) -> int:
#             if curr is None:
#                 return 1
            
#             pos = removeR(curr, curr.next, n)

#             if pos == n:
#                 prev.next = curr.next

            
#             return pos + 1
    
        
#         count = removeR(head, head.next, n)

#         if count <= n:
#             head = head.next

#         return head

#SAME SOLUTION BUT WITH n PASSED BY REFERENCE
# class Solution:
#     def rec(self, head, n):
#         if not head:
#             return None

#         head.next = self.rec(head.next, n)
#         n[0] -= 1
#         if n[0] == 0:
#             return head.next
#         return head

#     def removeNthFromEnd(self, head, n):
#         return self.rec(head, [n])



































            
        