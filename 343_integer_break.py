class Solution(object):
    def integerBreak(self, n):
        results = []
        if n == 2:
            return 1

        if n == 3:
            return 2

        for i in range(2, n/2 + 1):
            r = n / i
            remain = n % i
            results.append((r**(i-remain)) * ((r+1)**remain))
        return max(results)


s = Solution()
print s.integerBreak(10)
