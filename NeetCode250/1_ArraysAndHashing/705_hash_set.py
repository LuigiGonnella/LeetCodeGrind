
#!O(1) each operation, we could also used a linked list but O(N/K) each operation or BST (same O(N/k) worst case) where K = size of table (e.g. 10000 with 100 collision list)
class MyHashSet:

    def __init__(self):
        self.size = 1000000
        self.table = [-1] * self.size

        
    # def hash(self, key):

    #         if key < 0:
    #             key = - key
            
    #         return key % self.size

    def add(self, key: int) -> None:
        #self.table[self.hash(key)].append(key)
        self.table[key] = key
        

    def remove(self, key: int) -> None:
        # idx = self.hash(key)
        # tab = self.table[idx]
        # n = len(tab)
        # for i in range(n):
        #     if tab[i] == key:
        #         tab[i], tab[n - 1] = tab[n - 1], tab[i]
        #         tab.pop()
        #         return
        
        self.table[key] = -1

    def contains(self, key: int) -> bool:
        return self.table[key] != -1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)