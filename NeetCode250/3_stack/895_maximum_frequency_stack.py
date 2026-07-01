
#! MAP OF STACKS --> map of maxFreq : stack of elements with that freq
#this naturally keeps track of duplicates alements, inserting them at different frequencies as they come in
#so when we pop, we just pop from maxFreq key and decrease maxFreq by one (if "3" has a freq of "5", then it was also inserted in maxFreq key of "4", "3", "2", and "1")

#!O(1) time and O(N) space
class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stacks = {}
        self.maxFreq = 0
        

    def push(self, val: int) -> None: #!O(1)
        self.cnt[val] += 1
        currFreq = self.cnt[val]

        if currFreq > self.maxFreq:
            self.maxFreq = currFreq
            self.stacks[currFreq] = []
        
        self.stacks[currFreq].append(val)

    def pop(self) -> int: #!O(1)
        maxEl = self.stacks[self.maxFreq].pop()
        self.cnt[maxEl] -= 1

        if not self.stacks[self.maxFreq]:
            self.maxFreq -= 1
        
        return maxEl

#!O(N) time and space
class DoubleList:
    def __init__(self):
        self.head = self.tail = None
        

class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class FreqStack:

    def __init__(self):
        self.occ = defaultdict(int)
        self.dlist = DoubleList()
        

    def push(self, val: int) -> None:
        self.occ[val] += 1

        if not self.dlist.head:
            self.dlist.head = self.dlist.tail = ListNode(val)
        else:
            self.dlist.tail.next = ListNode(val, None, self.dlist.tail)
            self.dlist.tail = self.dlist.tail.next

        

    def pop(self) -> int: #!O(N)

        maxNode = None
        maxFreq = -1
        curr = self.dlist.tail

        while curr:

            if self.occ[curr.val] > maxFreq:
                maxFreq = self.occ[curr.val]
                maxNode = curr
            
            curr = curr.prev
        
        res = maxNode.val
        self.occ[res] -= 1
        

        if maxNode == self.dlist.head and maxNode == self.dlist.tail:
            self.dlist.head = self.dlist.tail = None
        elif maxNode == self.dlist.head:
            self.dlist.head = self.dlist.head.next
            self.dlist.head.prev = None
        elif maxNode == self.dlist.tail:
            self.dlist.tail.prev.next = self.dlist.tail.next
            self.dlist.tail = self.dlist.tail.prev
        else:
            maxNode.prev.next = maxNode.next
            maxNode.next.prev = maxNode
        
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



#!O(logN) time and O(N) space
# class FreqStack:

    def __init__(self):
        self.heap = []
        self.cnt = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        heapq.heappush(self.heap, (-self.cnt[val], -self.index, val))
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val



        

