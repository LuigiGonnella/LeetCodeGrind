class MyStack:

    def __init__(self): #!O(1)
        self.array = deque()
        self.size = 0
        

    def push(self, x: int) -> None: #!O(1)
        if (not self.array) or (len(self.array) <= self.size):
            self.array.append(x)
        else:
            self.array[self.size] = x

        self.size += 1
        

    def pop(self) -> int: #!O(1)
        el = self.array[self.size - 1]
        self.size -= 1
        return el
        

    def top(self) -> int: #!O(1)
        return self.array[self.size - 1]
        

    def empty(self) -> bool: #!O(1)
        return self.size == 0 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()