class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)

        r = []
        for k in cs.keys():
            r.append(ct.get(k, 0) - cs[k])
        posSum = sum([x for x in r if x > 0])
        negSum = abs(sum([x for x in r if x < 0]))
        return min(posSum, negSum) + abs(posSum - negSum)