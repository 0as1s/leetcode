class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        ones = Counter(s)['1']
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return (1 + (len(s) - 2)) * (len(s) - 2) // 2
        lc = 0
        ll = 0
        l = 0
        for i in range(len(s)):
            if s[i] == "1":
                lc += 1
                if lc == ones // 3:
                    ll = i
                if lc == (ones // 3 + 1):
                    l = i
        rc = 0
        rr = 0
        r = 0                    
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                rc += 1
                if rc == ones // 3:
                    rr = i
                if rc == (ones // 3 + 1):
                    r = i
        return (l-ll) * (rr-r)


s = Solution()
# print(s.numWays("100100010100110"))
# print(s.numWays('000'))
# print(s.numWays("0000"))
# print(s.numWays("10101"))
print(4049955000 % (10 ** 9 + 7))