class MyQueue:

    def __init__(self):
        self.N = 100
        self.size = self.N - 1
        self.head = self.tail = 0
        self.queue = [None] * self.N
        

    def push(self, x: int) -> None:
        if (self.tail + 1) % self.N == self.head: #full
            return

        
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.N
        

    def pop(self) -> int:
        el = self.queue[self.head]

        self.head = (self.head + 1) % self.N
        return el
        

    def peek(self) -> int:
        return self.queue[self.head]
        

    def empty(self) -> bool:
        return self.head == self.tail