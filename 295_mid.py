import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        temp = -heapq.heappop(self.lo)
        heapq.heappush(self.hi, temp)
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        return float(-self.lo[0]) if len(self.lo) > len(self.hi) else 0.5 * (-self.lo[0] + self.hi[0])

    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()