class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) == 1:
            return 0
        cur = points[0]
        total = 0
        for p in points[1:]:
            delta = [abs(p[0]-cur[0]), abs(p[1]-cur[1])]
            total += min(delta[0], delta[1])
            total += max(delta[0], delta[1]) - min(delta[0], delta[1])
            cur = p
        return  total

