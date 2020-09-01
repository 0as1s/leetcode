from functools import lru_cache
@lru_cache(-1)
def helper(n, last, cur, copied, wanted):
    print(n, last, cur, copied, wanted)
    if n == wanted:
        return cur
    if n + copied > wanted:
         return float("Inf")
    if last == 0: # copy
        return helper(n+copied, 1, cur+1, copied, wanted)
    else:
        return min(helper(n+copied, 1, cur+1, copied, wanted), helper(n, 0, cur+1, n, wanted))
    

class Solution(object):
    
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        return helper(1, 0, 1, 1, n)


s = Solution()
print(s.minSteps(3))