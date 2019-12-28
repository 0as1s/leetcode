class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        count = 0
        i = 0
        while miss <= n:
            if  i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                count += 1
        return count
s = Solution()
print(s.minPatches([1,2,3,8], 80))
