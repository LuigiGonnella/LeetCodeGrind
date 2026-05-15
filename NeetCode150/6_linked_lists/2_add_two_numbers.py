# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#!O(N) time and O(1) extra space (O(N) for output)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + carry    
          
            carry = val // 10
            val = val % 10 

            curr.next = ListNode(val, None)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

            
        
        return dummy.next

#O(N) time and O(N) extra space (O(2*N) for output + stack)
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#         def addR(head: Optional[ListNode], l1: Optional[ListNode], l2: Optional[ListNode], carry: int):
#             if l1 is None and l2 is None and not carry:
#                 return 
            
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             val = val1 + val2 + carry
#             carry = val // 10

#             val = val % 10

#             head.next = ListNode(val)

#             return addR(head.next, l1.next if l1 else None, l2.next if l2 else None, carry)



            
#         dummy = ListNode()
#         addR(dummy, l1, l2, 0)

#         return dummy.next
        