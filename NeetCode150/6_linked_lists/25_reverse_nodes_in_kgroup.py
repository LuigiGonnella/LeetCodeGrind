# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#ITERATIVE SOLUTION --> O(N) time, O(1) space
# class Solution:
#     def _reverse(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         revHead = None
#         y = head
#         count = 0
#         lastNext = None
#         newLast = None
#         originalLast = None

#         while y and count < k:
#             count += 1
#             t = y.next
#             if count == k:
#                 lastNext = t 

#             y.next = revHead
#             revHead = y
#             if count == 1:
#                 newLast = revHead
#             y = t

#         if count < k: #reverse again
#             y = revHead
#             head = None
#             originalLast = None
#             while y:
#                 if originalLast is None:
#                     originalLast = y
#                 t = y.next
#                 y.next = head
#                 head = y
#                 y = t

#             return head, None, originalLast
            

            

        
#         return revHead, lastNext, newLast



#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if k <= 1 or not head:
#             return head
        
#         dummy = ListNode()
#         dummy.next = head
#         res = dummy
#         while res.next:
#             #reverse k (handle less thank K in subgroup)
#             res.next, lastNext, newLast = self._reverse(res.next, k)
#             #link with next original (keep original subgroup head and link it with next subgroup)
#             newLast.next = lastNext
#             #update res with first of next subgroup
#             res = newLast
        
#         return dummy.next


#CLEANER ITERATIVE SOLUTION --> O(N) time, O(1) space
# class Solution:
#     def reverseKGroup(self, head, k):
#         dummy = ListNode(0)
#         dummy.next = head
#         groupPrev = dummy

#         while True:
#             # find kth node
#             kth = groupPrev
#             for _ in range(k):
#                 kth = kth.next
#                 if not kth:
#                     return dummy.next

#             groupNext = kth.next

#             # reverse group
#             prev, curr = groupNext, groupPrev.next
#             while curr != groupNext:
#                 tmp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = tmp

#             tmp = groupPrev.next
#             groupPrev.next = kth !connect reversed group to the PREVIOUS group (for the first i attach DUMMY to the new head)
#             groupPrev = tmp

#RECURSIVE SOLUTION --> O(N) time, O(N/K) space (STACK)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for _ in range(k):
            if not curr:    
                return head
            curr = curr.next #curr diventa primo elemento next group
        
        prev = self.reverseKGroup(curr, k) #prev = next giusto dell'ultimo elemento gruppo attuale da invertire
        #esso e il rsultato della ricorsione (inversione) del next group, quindi il primo del reversed group
        #questo dovra essere il next dell'ultimo elemento dell'attuale reversed group

        while head != curr: #curr = next dell'ultimo elemento del gruppo che sto invertendo, lo uso
            #come condizione di terminazione del gruppo da invertire
            #questo next originale, viene sostituito nel while con il next giusto, ma prendo il next vecchio (tmp) e lo confronto con il next originale (curr)
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        return prev



        
        


    



















        