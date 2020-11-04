from heapq import *
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        stones = [-x for x in stones]
        heapify(stones)
        while True:
            t1 = heappop(stones)
            t2 = heappop(stones)
            if not stones:
                return max(t1, t2) - min(t1, t2)
            if t1 - t2 != 0:
                heappush(stones, min(t1, t2) - max(t1, t2))
            else:
                if len(stones) == 1:
                    return -stones[0]