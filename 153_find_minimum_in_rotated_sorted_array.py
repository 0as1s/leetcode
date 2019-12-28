class Solution(object):

    def findMin(self, nums):
        length = len(nums)
        if length <= 20:
            return min(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return min(nums[0], nums[1])
        l = 0
        r = length - 1
        if nums[l] < nums[(l + r) / 2] < nums[r]:
            return nums[0]

        while(True):
            m = (l + r) / 2
            if m == r or m == l:
                return min(nums[r], nums[l])
            if nums[m] > nums[l]:
                l = m
            else:
                r = m


s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print s.findMin(nums)

nums = [2, 0, 1]
print s.findMin(nums)

nums = [2, 1]
print s.findMin(nums)

nums = [0]
print s.findMin(nums)

nums = [1, 2, 3]
print s.findMin(nums)

nums = [2, 3, 1]
print s.findMin(nums)
