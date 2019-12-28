class Solution(object):

    def uniquePaths(self, m, n):
        m = m - 1
        n = n - 1
        if n == 0 or m == 0:
            return 1
        result = 1
        max_ = max(m, n)
        for i in range(m + n, max_, -1):
            result *= i
        for j in range(1, m + n - max_ + 1):
            result /= j
        return result


s = Solution()
print s.uniquePaths(3, 7)
