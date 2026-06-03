# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#!O(N) time and O(1) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        if not head:
            return 0

        slow, fast = head, head

        #O(N)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #revert slow
        def reverse(h):
            new_head = None

            curr = h
            while curr:
                tmp = curr.next
                curr.next = new_head
                new_head = curr

                curr = tmp
            
            return new_head
        
        slow_inv = reverse(slow) #O(N)
        
        
        maxSum = float("-inf")
        while slow_inv: #O(N)
            maxSum = max(maxSum, head.val + slow_inv.val)
            head = head.next
            slow_inv = slow_inv.next
        
        return maxSum
        


        