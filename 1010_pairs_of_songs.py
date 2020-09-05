class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        r = 0
        sums = [60 * i for i in range(1000//60)]
        for t in time:
            for s in sums:
                if s-t in d:
                    r += d[s-t]
            d[t] += 1
        return r
