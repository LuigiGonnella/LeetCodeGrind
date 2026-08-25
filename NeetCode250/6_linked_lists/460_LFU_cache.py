class Node:
    def __init__(self, val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    

class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {} #key: k, value: (v, counter, node in usage val)
        self.usage = {} #key: counter, value: double linked list with cache entries
        self.minCnt = 0
        self.capacity = capacity
        self.size = 0 #actual number of elements
        

    #delete the given node in the give dll
    def _delete_node(self, dll, node) -> bool: #empty or not after deletion
        if not dll.head:
            return True
        
        if dll.head == dll.tail: #single node
            dll.head = dll.tail = None
            return True
        
        if dll.head == node: #head deletion
            dll.head = dll.head.next
            dll.head.prev = None

        elif dll.tail == node: #tail deletion
            dll.tail = dll.tail.prev
            dll.tail.next = None
        
        else: #middle deletion
            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = node.prev = None
        

        return False


    #add in head, the entry of key in the given dll
    def _add_node(self, dll, key) -> Node:
        dll.head = Node(key, dll.head, None)
        if dll.head.next: #if prev head existed
            dll.head.next.prev = dll.head
        else: #now we have only a single node
            dll.tail = dll.head

        return dll.head

    
    #delete from self.minCnt (LFU) from tail (LRU amonf LFUs)
    def _delete_lfu(self) -> None:

        dll = self.usage[self.minCnt]
        self.cache[dll.tail.val] = None

        if dll.tail == dll.head: #if only one node
            dll.tail = dll.head = None
            self.minCnt += 1
        else:
            #more than one node
            dll.tail = dll.tail.prev
            dll.tail.next = None
        
        self.size -= 1

         

    def get(self, key: int) -> int:
        if key in self.cache and self.cache[key]:
            val = self.cache[key][0] #get val

            currCnt = self.cache[key][1] #get curr cnt
            newCnt = currCnt + 1 #set new cnt
            old_node = self.cache[key][2] #get old node
            

            old_dll = self.usage[currCnt] #get old dll
            if newCnt not in self.usage :
                self.usage[newCnt] = DoubleLinkedList()
            
            new_dll = self.usage[newCnt] #get new dll


            is_empty = self._delete_node(old_dll, old_node) #delete from previous dll
            new_node = self._add_node(new_dll, key) #add in head of new dll --> list goes from most recent (head) to least recent (tail)

            self.cache[key][1] = newCnt #update counter
            self.cache[key][2] = new_node #update node

            if is_empty and self.minCnt == currCnt:
                self.minCnt += 1

            return val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
            
        if (key not in self.cache or not self.cache[key]) and self.size == self.capacity: #full, we have to delete LFU
            self._delete_lfu()

        newCnt = None
        if key in self.cache and self.cache[key]:
            #delete from oldCnt
            #newCnt = oldCnt + 1

            currCnt = self.cache[key][1] #get curr cnt
            newCnt = currCnt + 1 #set new cnt
            old_node = self.cache[key][2] #get old node
            

            old_dll = self.usage[currCnt] #get old dll
            


            is_empty = self._delete_node(old_dll, old_node) #delete from previous dll
            

            if is_empty and self.minCnt == currCnt:
                self.minCnt += 1


        else: #update size, reset minCnt, set newCnt = 1
           
            self.cache[key] = [-1] * 3
            self.size += 1
            self.minCnt = 1
            newCnt = 1
            self.cache[key][1] = newCnt
        
        #add to newCnt
        if newCnt not in self.usage:
            self.usage[newCnt] = DoubleLinkedList()
        
        new_dll = self.usage[newCnt] #get new dll
        new_node = self._add_node(new_dll, key) #add in head of new dll --> list goes from most recent (head) to least recent (tail)

        self.cache[key][0] = value
        self.cache[key][1] = newCnt #update counter
        self.cache[key][2] = new_node #update node
        

            

            

        

            

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)