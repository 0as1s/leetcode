import bisect

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l = 0
        r = len(nums) - 1
        pivot = -1
        if nums[-1] > nums[0]:
            i = bisect.bisect_left(nums, target)
            if i < len(nums):
                return nums[i] == target
            return False
        while l != r and r-l != 1:
            m = (l+r) // 2
            if nums[m] > nums[m+1]:
                pivot = m
                break
            else:
                if nums[m] < nums[0]:
                    r = m
                else:
                    l = m
        if pivot == -1:
            return nums[0] == target
        i1 = bisect.bisect_left(nums[:pivot+1], target)
        if i1 <= pivot and nums[:pivot+1][i1] == target:
            return True
        i2 = bisect.bisect_left(nums[pivot+1:], target)
        if i2 < len(nums[pivot+1:]) and nums[pivot+1:][i2] == target:
            return True
        return False

s = Solution()
print(s.search( nums = [2,5,6,0,0,1,2], target = 3))
print(s.search(nums = [2,5,6,0,0,1,2], target = 0))
print(s.search(nums = [0, 0], target = 1))