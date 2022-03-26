class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []

    def addNum(self, num: int) -> None:
        self.ls.append(num)

    def findMedian(self) -> float:
        self.ls.sort()
        if len(self.ls) % 2 == 1:
            return self.ls[int(len(self.ls) / 2)]
        else:
            return (self.ls[int(len(self.ls) / 2) - 1] + self.ls[int(len(self.ls) / 2)]) / 2
