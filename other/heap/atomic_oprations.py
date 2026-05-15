
class HeapNode:
    def __init__(self, key = 0, value = ""):
        self.key = key
        self.value = value
    
class Heap:
    def __init__(self):
        self.nodes = [] #array of the BT by level
        self.size = 0
    
    def fill(self, node: HeapNode):
        self.nodes.append(node) #we just insert, so it's not sure this will be an heap anymore (we will need heapify)
        self.size += 1
    
    def heapify(self, i: int):
        n = self.size
        largest = i

        if (2*i + 1) < n and self.nodes[2*i + 1].key > self.nodes[largest].key:
            largest = 2*i + 1
        
        if (2*i + 2) < n and self.nodes[2*i + 2].key > self.nodes[largest].key:
            largest = 2*i + 2
        
        if largest != i:
            self.nodes[i], self.nodes[largest] = self.nodes[largest], self.nodes[i] 
            self.heapify(largest)
    
    def heapbuild(self):

        def parent(i):
            return (i - 1) / 2
        
        for i in range(parent(self.size - 1), -1, -1):
            self.heapify(i)
    


#!RECURSIVE HEAPSORT
def heapsort(nums: List[int]) -> List[int]: #ascending order
    heap = Heap()
    for num in nums:
        heap.fill(HeapNode(num))

    heap.heapbuild()

    def dfs():
        n = heap.size

        if n > 1:
            heap.nodes[0], heap.nodes[n - 1] = heap.nodes[n - 1], heap.nodes[0]

            heap.size -= 1
            heap.heapify(0)
            dfs()
    
    dfs()
    return heap.nodes


#!ITERATIVE HEAPSORT
def heapsort(nums: List[int]) -> List[int]: #ascending order
    heap = Heap()
    for num in nums:
        heap.fill(HeapNode(num))

    heap.heapbuild()

    for i in range(heap.size -1, 0, -1):
        heap.nodes[0], heap.nodes[i] = heap.nodes[i], heap.nodes[0]
        heap.size -= 1
        heap.heapify(0)
    
    return heap.nodes      

#!PRIORITY QUEUE (using heap)
class HeapNode:
    def __init__(self, prio = 0, key = ""): #prio is the priority
        self.prio = prio
        self.key = key
    
class PQ:
    def __init__(self):
        self.nodes = [] #array of the BT by level
        self.size = 0
    
    def fill(self, key, prio):
        self.nodes.append(HeapNode(key, prio)) #we just insert, so it's not sure this will be an heap anymore (we will need heapify)
        self.size += 1
    
    def heapify(self, i: int):
        n = self.size
        largest = i

        if (2*i + 1) < n and self.nodes[2*i + 1].prio > self.nodes[largest].prio:
            largest = 2*i + 1
        
        if (2*i + 2) < n and self.nodes[2*i + 2].prio > self.nodes[largest].prio:
            largest = 2*i + 2
        
        if largest != i:
            self.nodes[i], self.nodes[largest] = self.nodes[largest], self.nodes[i] 
            self.heapify(largest)
    
    def heapbuild(self):

        def parent(i):
            return (i - 1) // 2
        
        for i in range(parent(self.size - 1), -1, -1):
            self.heapify(i)
    
    def showMax(self) -> HeapNode:
        return self.nodes[0]

    def insert(self, key, prio):

        def parent(i):
            return (i - 1) // 2
        
        self.fill(key, prio)
        i = self.size - 1

        while i > 0 and self.nodes[parent(i)].prio < self.nodes[i]:
            self.nodes[parent(i)], self.nodes[i] = self.nodes[i], self.nodes[parent(i)]
            i = parent(i)
    
    def extractMax(self) -> HeapNode:
        
        res = self.nodes[0]
        n = self.size
        self.nodes[0] = self.nodes[n - 1]
        self.nodes.pop()
        self.size -= 1

        if self.size > 1:
            self.heapify(0)

        return res
        
    
    def change_priority(self, new_prio, key): #it is O(N) because of linear iteration to find pos
        #if we embed pos in HeapNode this would be O(logN)

        #find pos
        pos = -1
        for i in range(self.size):
            if self.nodes[i].key == key:
                pos = i
                break
        
        if pos == -1:
            return

        def parent(i):
            return (i - 1) // 2

        self.nodes[pos].prio = new_prio

        #switch with parent until no more lower parents are found
        while pos > 0 and self.nodes[parent(pos)].prio < self.nodes[pos].prio:
            p = parent(pos)
            self.nodes[p], self.nodes[pos] = self.nodes[pos], self.nodes[p] 
            pos = p
        
        #or do heapify
        self.heapify(pos)

        #it looks like we are doing both but 
        #if I go UP (new_prio > prio), then heapify will return without doing anything
        #if I go DOWN (new_prio < prio), then the we will never enter in the while loop


