class Solution(object):

    def titleToNumber(self, s):
        l = len(s)
        t = 0
        import math
        for i, c in enumerate(s):
            t += (ord(c) - ord('A') + 1) * math.pow(26, l - i - 1)
        return int(t)


s = Solution()
print s.titleToNumber('AAA')
