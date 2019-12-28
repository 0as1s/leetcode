class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = True if x < 0 else False
        r = int("".join(list(reversed(str(abs(x))))))
        if negative:
            r = -r
        if not -2**31 <= r < 2**31:
            return 0
        return r

