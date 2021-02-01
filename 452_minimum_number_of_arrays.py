from heapq import *
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = [[x[1], x[0]] for x in points]
        heapify(points)
        m = -float("Inf")
        count = 0
        while points:
            p = heappop(points)
            print(p, m)
            if p[1] > m:
                count += 1
                m = p[0]
        return count
