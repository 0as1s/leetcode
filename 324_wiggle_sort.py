class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copyed = sorted(nums)
        i = 0
        j = 0
        while i<len(nums):
            nums[i] = copyed[j]
            j += 1
            i += 2
        j = len(nums) - 1
        while i < len(nums):
            nums[i] = copyed[j]
            j -= 1
            i += 2
