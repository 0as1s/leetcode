class Solution(object):

    def moveZeroes(self, nums):
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        for i in range(len(nums)):
            if nums[i] != 0:

nums = [0, 1, 0, 3, 12]
# nums = [0, 1, 0]
# nums = [0, 0, 1]

s = Solution()
s.moveZeroes(nums)
print nums
