class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.ls = []
        self.size = size
    def next(self, val: int) -> float:
        self.ls.append(val)
        if len(self.ls) > self.size:
            self.ls.pop(0)
        return sum(self.ls) / len(self.ls)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == '__main__':
    m = MovingAverage(3)
    print(m.next(1))  # = 1
    print(m.next(10))  # = (1 + 10) / 2  = 5.5
    print(m.next(3))  # = (1 + 10 + 3) / 3  = 4.666666666666667
    print(m.next(5))  # = (10 + 3 + 5) / 3 = 6.0
