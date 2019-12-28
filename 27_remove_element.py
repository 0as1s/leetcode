class Solution(object):

    def removeElement(self, nums, val):
        count = 0
        for i in xrange(len(nums)):
            if nums[i] == val:
                nums[i] = None
                count += 1
        for i in range(count):
            for i in xrange(len(nums) - 1):
                if nums[i] is None:
                    for j in xrange(i, len(nums) - 1, 1):
                        nums[j] = nums[j + 1]
        return len(nums) - count


s = Solution()
print s.removeElement([2, 2, 3], 2)
