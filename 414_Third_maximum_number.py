class Solution(object):

    def thirdMax(self, nums):
        source = max(nums)
        for i in range(2):
            a = max(nums)
            for j in range(len(nums)):
                if nums[j] == a:
                    nums[j] = None
        m = max(nums)
        if m is None:
            return source
        else:
            return m


nums = [2, 2, 3, 1]
nums = [1, 2]
nums = [3, 2, 1]
nums = [1, 2, -2147483648]
s = Solution()
print s.thirdMax(nums)
