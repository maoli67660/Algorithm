class MaxQueue:

    def __init__(self):
        self.dequeue = []
        self.q = []

    def max_value(self) -> int:
        if not self.dequeue:
            return -1
        return self.dequeue[0]

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while len(self.dequeue)!=0 and self.dequeue[-1] < value:
            self.dequeue.pop()
        self.dequeue.append(value)

    def pop_front(self) -> int:
        if not self.q:
            return -1
        top = self.q.pop(0)
        if top == self.dequeue[0]:
            self.dequeue.pop(0)
        return top


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()