class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        n = sorted(nums)
        i = 0
        j = len(nums) - 1
        while (n[i] == nums[i]):
            i += 1
            if i == len(nums)-1:
                return 0
        while (n[j] == nums[j]):
            j -= 1
        return j - i + 1

print Solution().findUnsortedSubarray([2, 6, 4, 10, 8, 10, 15])
