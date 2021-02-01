class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums) % 2 == 1:
            r = 0
            mid = nums[len(nums)//2]
            for i in range(len(nums)):
                r += abs(mid - nums[i])
            return r
        else:
            r1 = 0
            r2 = 0
            mid1 = nums[len(nums)//2]
            mid2 = nums[len(nums)//2 + 1]
            for i in range(len(nums)):
                r1 += abs(mid1 - nums[i])
                r2 += abs(mid2 - nums[i])
            return min(r1,  r2)
