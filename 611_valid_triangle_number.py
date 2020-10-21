class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from bisect import *
        nums = sorted(nums)
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+2, len(nums)):
                k = bisect_left(nums, nums[j] - nums[i] + 1, i+1, j)
                count += j - k
        return count