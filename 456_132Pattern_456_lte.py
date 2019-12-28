class Solution(object):

    def find132pattern(self, nums):
        if not nums:
            return False
        min_ = 9999
        i = 0
        while i < len(nums) - 2:
            if not nums[i + 1] <= nums[i]:
                min_ = nums[i]
                for j in range(i, len(nums) - 1):
                    if not nums[j + 1] >= nums[j]:
                        max_ = nums[j]
                        for k in range(j, len(nums)):
                            if min_ < nums[k] < max_:
                                return True
                        i = j
                        break
            i += 1
        return False


s = Solution()
print s.find132pattern([-1, 3, 2, 0])
print s.find132pattern([3, 1, 4, 2])
print s.find132pattern([90, 100, 50, 70, 20, 40, 10, 51])
