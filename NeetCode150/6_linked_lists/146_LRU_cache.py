
#!DOUBLED LINKED LIST --> EVERY OPERATION IS O(1)
class ListNode:
    def __init__(self, val: int = 0, next: ListNode =  None, prev: ListNode = None) -> ListNode:
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0 #actual number of elements
        self.capacity = capacity #maximum number of elements
        self.hmap = {} #key = int, value = [int, ListNode]
        self.head = None
        self.tail = None 
    
    def _deleteNode(self, curr: ListNode) -> None: #handle the head scenario
        if curr == self.head and curr == self.tail: #when they are the same
            self.head = self.tail = None 
            return

        if curr == self.head:
            self.head = self.head.next
            self.head.prev = None
            return

        if curr == self.tail:
            newTail = curr.prev
            newTail.next = None
            self.tail = newTail
            return
        
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        

    def _insertNodeHead(self, curr: ListNode) -> None:
        if self.head is None:
            curr.prev = curr.next = None
            self.head = self.tail = curr
            return
        
        curr.next = self.head
        self.head.prev = curr
        curr.prev = None
        self.head = curr
        


    def get(self, key: int) -> int:
        if key in self.hmap:
            if key != self.head.val: #not already most recent
                self._deleteNode(self.hmap[key][1])
                self._insertNodeHead(self.hmap[key][1])
            return self.hmap[key][0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:    
        if key in self.hmap:
            self._deleteNode(self.hmap[key][1])
            self.hmap[key][0] = value
            self.size -= 1
        else:
            self.hmap[key] = [value, ListNode(key)]
            if self.size >= self.capacity:
                del self.hmap[self.tail.val]
                self._deleteNode(self.tail) 
                self.size -= 1
                
        
        self._insertNodeHead(self.hmap[key][1])              
        self.size += 1

        
