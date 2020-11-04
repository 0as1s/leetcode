class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        s = sum(nums)
        ls = 0
        for i in range(1, len(nums)-1):
            ls += nums[i-1]
            if ls == s - ls - nums[i]:
                return i
        return -1