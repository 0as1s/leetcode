class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        a = []
        for w in wall:
            s = 0
            for i in wall[:-1]:
                s += i
                a.append(s)
        c = Counter(a)
        return len(wall) - max(c.values())
