# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(N) time
#O(1) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        y = head
        rev_head = None

        while y:
            t = y.next

            y.next = rev_head
            rev_head = y

            y = t
        
        return rev_head
