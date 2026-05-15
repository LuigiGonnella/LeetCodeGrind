# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(N+M)
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 or list2

        return dummy.next

            





#O(N*M)
# class Solution:
#     def _sortedInsertion(self, list2: Optional[ListNode], val: int):
#         if list2 is None or val < list2.val:
#             list2 = ListNode(val, list2)
#             print(list2.val)
#             return list2

#         prev = list2
#         curr = list2.next

#         while curr and curr.val < val:
#             prev = curr
#             curr = curr.next
        
        
#         prev.next = ListNode(val, curr)
#         return list2


#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         curr = list1

#         while curr:
#             list2 = self._sortedInsertion(list2, curr.val)
#             curr = curr.next
        
#         return list2
        