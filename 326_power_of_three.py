class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n != 3:
            n /= 3
            if n != int(n):
                return False
            n = int(n)
            if n < 3:
                return False
        return True

print(Solution().isPowerOfThree(19684))