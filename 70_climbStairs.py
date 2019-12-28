class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        left = 1
        right = 2
        for i in range(n-2):
            new_ = left + right
            left = right
            right = new_
        return right

s = Solution()
print(s.climbStairs(3))
