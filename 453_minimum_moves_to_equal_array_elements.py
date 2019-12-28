class Solution(object):

    def minMoves(self, nums):
        m = min(nums)
        s = 0
        for d in nums:
            s += (d - m)
        return s


s = Solution()
print s.minMoves([1, 2, 3])
