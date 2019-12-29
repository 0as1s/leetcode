class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return "1" not in bin(n).replace("0b", "")[1:]


s = Solution()
print(s.isPowerOfTwo(1))