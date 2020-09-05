class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        c = Counter(s)
        print(c)
        s = sorted(list(c.values()), reverse=True)
        print(s)
        print(sum(s))
        flag = False
        r = 0
        for ss in s:
            if ss % 2 != 0:
                if not flag:
                    r += ss
                    flag=True
                else:
                    r += ss - 1
            else:
                r += ss
        return r
s = Solution()
