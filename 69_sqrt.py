class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in (0, 1):
            return x
        r = x // 2
        left = 0
        right = x
        while True:
            r = (left + right) // 2
            if r ** 2 <= x < (r+1) ** 2:
                return r
            elif r ** 2 > x:
                right = r
            else:
                left = r

s = Solution()
print(s.mySqrt(2147395599))

