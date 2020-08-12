class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        if len(s) < k:
            return False
        c = Counter(s)
        odds = len([x for x in c.keys() if c[x] % 2 == 1])
        if odds > k:
            return False
        return True

s = Solution()
print(s.canConstruct(s = "annabelle", k = 2))
print(s.canConstruct(s = "leetcode", k = 3))
print(s.canConstruct(s = "true", k = 4))
print(s.canConstruct(s = "yzyzyzyzyzyzyzy", k = 2))
