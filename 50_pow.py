from functools import lru_cache

@lru_cache(32)
def fastPow(x, n):
    if n == 1:
        return x
    if n == 0:
        return 1.0
    else:
        if n % 2 == 0:
            return fastPow(x, n//2) * fastPow(x, n//2)
        else:
            return fastPow(x, n//2) * fastPow(x, n//2) * x
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return 1 / fastPow(x, abs(n))
        return fastPow(x, n)

s = Solution()
print(s.myPow(2.00000, -2))