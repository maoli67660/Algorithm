import heapq as h


class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        self.pq = self.nums[:3]
        h.heapify(self.pq)
        for i in self.nums[3:]:
            self.add(i)

    def add(self, val):
        if len(self.pq) < self.k:
            h.heappush(self.pq, val)
        else:
            if self.pq[0] < val:
                h.heappop(self.pq)
                h.heappush(self.pq, val)

        print(self.pq)
        return self.pq[0]


if __name__ == '__main__':
    k = 3
    arr = []
    kthLargest = KthLargest(k, arr)
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))
    print(kthLargest.add(8))
    print(kthLargest.add(7))
    print(kthLargest.add(6))
