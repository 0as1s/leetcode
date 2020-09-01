def f(n):
    nums = []
    while n != 0:
        nums.append(n % 10)
        n //= 10
    return sum(x*x for x in nums)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        visited.add(n)
        while True:
            n = f(n)
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
