class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        r = 0
        m = 1
        for i in reversed(s):
            m = max(m, d[i])
            if d[i] < m:
                r -= d[i]
            else:
                r += d[i]
        return r
