class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return list(str(x)) ==  list(reversed(str(x)))
