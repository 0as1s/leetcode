from heapq import *
from collections import *

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 0
        def dis(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        distances = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                heappush(distances[i], (dis(points[i], points[j]), j))
                heappush(distances[j], (dis(points[i], points[j]), i))
        visited = set([0,])
        unvisited = set(list(range(1, len(points))))
        cost = 0
        while unvisited:
            candidates = []
            for v in visited:
                if not v in distances:
                    continue
                dis = distances[v]
                while dis and dis[0][1] in visited:
                    heappop(dis)
                distances[v] = dis
                heappush(candidates, dis[0])
            cost += candidates[0][0]
            visited.add(candidates[0][-1])
            unvisited.remove(candidates[0][-1])
        return cost
s = Solution()
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(s.minCostConnectPoints([[0, 0], [1, 1]]))
print(s.minCostConnectPoints([[0, 0]]))
print(s.minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))
