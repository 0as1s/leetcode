class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        r = 0        
        c = defaultdict(int)
        for x, y in dominoes:
            if (x, y) in c:
                r += c[(x, y)]
            if x != y:
                if (y, x) in c:
                    r += c[(y, x)]
            c[(x, y)] += 1
        return r
