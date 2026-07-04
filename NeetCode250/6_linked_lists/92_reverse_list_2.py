# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#!O(N) time and O(1) space
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        l = left - 1
        first = head
        prev = None

        while first and l: #first = first node, prev = previous one
            prev = first
            first = first.next
            l -= 1
    
        r = right - 1
        last = head

        while last and r: #last = last node
            last = last.next
            r -= 1
        

        newL = None
        curr = first
        end = last.next #when curr == end we stop reverting the list


        while curr != end:
            tmp = curr.next

            curr.next = newL
            newL = curr

            curr = tmp
        
        #now in newL we got the [left: right + 1] reversed list
        
        if prev: #attach initial prev to new first (reversed list head)
            prev.next = newL
        else: #if no prev it means we reverted from head, so new head is reversed list head
            head = newL
        
        first.next = end #first has the old first node, that now is the last one in the reversed list, so attach it to original follower of original last 

        return head
        




        