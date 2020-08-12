class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2 == 0:
            return (1 + n-1) * (n // 2) // 2
        else:
            return (0 + n-1) * ((n+1)//2)//2
