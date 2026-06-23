
#!O(N/K) where N = #elements and K = 10000 (table dim)
class ListNode:
    def __init__(self, key, val, nxt = None):
        self.key = key
        self.val = val
        self.nxt = nxt
    

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size
        
    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)

        curr = self.table[idx]
        while curr:
            if curr.key == key:
                curr.val = value
                return

            curr = curr.nxt
        
        #head insertion
        self.table[idx] = ListNode(key, value, self.table[idx])
        

    def get(self, key: int) -> int:
        idx = self.hash(key)

        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.val
            
            curr = curr.nxt
        
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.hash(key)

        prev = self.table[idx]
        if not prev:
            return 

        if key == prev.key:
            self.table[idx]= self.table[idx].nxt 
            return

        curr = prev.nxt

        while curr:
            if curr.key == key:
                prev.nxt = curr.nxt
                return

            prev = curr
            curr = curr.nxt
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)