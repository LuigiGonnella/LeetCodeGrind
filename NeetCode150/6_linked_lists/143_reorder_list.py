# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(N) time
#O(N) space
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:

#         def reorderR(root: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
#             if curr is None:
#                 return root

#             root = reorderR(root, curr.next)

#             if root is None:
#                 return None
            
#             tmp = None
#             if root == curr or root.next == curr:
#                 curr.next = None
#             else:
#                 tmp = root.next
#                 root.next = curr
#                 curr.next = tmp
            
#             return tmp
        
#         reorderR(head, head.next)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        second = slow.next
        slow.next = None
        
        def reverseList(root: Optional[ListNode]) -> Optional[ListNode]:
            y = root
            revHead = None

            while y:
                tmp = y.next
                y.next = revHead
                revHead = y

                y = tmp
            
            return revHead

        
        #second is the head of second half 
        secondRev = reverseList(second) 
    
        def mergeList(secondRev: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
            first = head
            second = secondRev

            while second:
                tmp1 = first.next
                tmp2 = second.next
                first.next = second
                second.next = tmp1
                first = tmp1
                second = tmp2



            #first.next = second
            return first

        head = mergeList(secondRev, head)



            



        