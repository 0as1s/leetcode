class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        cur = 1
        to_compare = []
        from collections import Counter
        while cur < 10**len(str(N)):
            to_compare.append(Counter(str(cur)))
            cur = cur << 1
        N = Counter(str(N))
        for t in to_compare:
            if N == t:
                return True
        return False
