from functools import lru_cache

@lru_cache(999999)
def helper(x, y, t, N):
    dir = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    s = 0
    if t == 0:
        for d in dir:
            if 0 <= x+d[0] < N and 0 <= y+d[1] < N:
                s += 1.0 / 8.0
        return s
    else:
        for d in dir:
            if 0 <= x+d[0] < N and 0 <= y+d[1] < N:
                s += (1.0 / 8.0) * helper(x+d[0], y+d[1], t-1, N)
        return s
    
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        return helper(r, c, K-1, N)