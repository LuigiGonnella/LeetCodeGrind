# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#IF WE TAKE THE MINIMUM AMONG FIRST K indexes and then move the chosen index ahead, for N times --> O(N*K)


# HEAP SOLUTION --> O(NlogK), O(K) space
# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         K = len(lists)
#         heap = []
#         dummy = ListNode()
#         currNew = dummy

#         for i in range(K):
#             if lists[i]:
#                 heapq.heappush(heap, (lists[i].val, 0, i))
        
#         while heap:
#             minEl = heapq.heappop(heap)
#             currNode = lists[minEl[2]]
#             if currNode.next:
#                 heapq.heappush(heap, (currNode.next.val, minEl[0] + 1, minEl[2]))
#                 lists[minEl[2]] = currNode.next


#             currNew.next = currNode
#             currNew = currNode
        
#         return dummy.next

# DIVIDE & CONQUER ITERATIVE SOLUTION --> O(NlogK), O(K) space (MERGED ARRAY)
# class Solution: 
#     def _twoWayMerge(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         curr = dummy
#         while head1 and head2:
#             if head2.val < head1.val:
#                 curr.next = head2
#                 head2 = head2.next
#             else:
#                 curr.next = head1
#                 head1 = head1.next
            
#             curr = curr.next
        
#         curr.next = head1 or head2
        
#         return dummy.next



#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None

#         while len(lists) > 1:
#             merged = []
#             for k in range(0, len(lists), 2):
#                 l1 = lists[k]
#                 l2 = lists[k + 1] if (k + 1) < len(lists) else None
#                 newList = self._twoWayMerge(l1, l2) 
#                 merged.append(newList)
            
#             lists = merged
        
#         return lists[0]

# DIVIDE & CONQUER RECURSIVE SOLUTION --> O(NlogK), O(logK) space (STACK)
class Solution: 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists, 0, len(lists) - 1)



    
    def divide(self, lists: List[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
        if l > r:
            return None
        
        if l == r:
            return lists[l]
        
        m = l + (r - l) // 2

        left = self.divide(lists, l, m) #i cannot switch writing (l, m - 1) left and (m, r) right because of the rounding down of int division
        #when, after rounding down (es. m = (1 + 2) // 2 = 1), m == l, with the correct solution i will recurr with l == r in left and l == r in right
        #but with the wrong version i would recurr with different l <  r in left (not ok) and with the same l and r in rigth !(infinite recursion)
        right = self.divide(lists, m + 1, r)

        return self.conquer(left, right)

    
    
    
    def conquer(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]: #TWO WAY MERGE
        dummy = ListNode()
        curr = dummy
        while head1 and head2:
            if head2.val < head1.val:
                curr.next = head2
                head2 = head2.next
            else:
                curr.next = head1
                head1 = head1.next
            
            curr = curr.next
        
        curr.next = head1 or head2
        
        return dummy.next





        