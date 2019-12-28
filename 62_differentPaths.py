class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n ==0:
            return 0
        i = 1
        for j in range(max(m, n), m+n-1):
            i *= j
        for j in range(2, min(m, n)):
            i /= j
        return int(i)

s = Solution()
print(s.uniquePaths(2, 2))