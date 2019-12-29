from collections import Counter, defaultdict


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        degree = max(Counter(nums).values())
        d = defaultdict(int)
        l, r = 0, 0
        m = float("Inf")
        for r in range(len(nums)):
            d[nums[r]] += 1
            while d[nums[r]] == degree:
                m = min(m, r-l+1)
                d[nums[l]] -= 1
                l += 1
            # print(d)
        return m


s = Solution()
a = [1, 2, 2, 3, 1]
a = [1,]
print(s.findShortestSubArray(a))
