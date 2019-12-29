from bisect import bisect_left


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if target == nums[0]:
                return 0
            elif target == nums[1]:
                return 1
            return -1
        left = 0
        r = len(nums) - 1
        has_reversed = False
        split = len(nums)
        while left != r:
            m = (left + r) // 2
            if m == len(nums) - 1:
                # print(left)
                # print(m)
                break
            if nums[m] > nums[m+1]:
                has_reversed = True
                split = m+1
                break
            elif nums[m] > nums[-1]:
                left = m + 1
            else:
                r = m
        # print(split)
        if not has_reversed:
            i = bisect_left(nums, target)
            if i >= len(nums):
                return -1
            return i if nums[i] == target else -1
        if target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            i = bisect_left(nums[:split], target)
            if i >= len(nums):
                return -1
            return i if nums[i] == target else -1
        else:
            i = bisect_left(nums[split:], target)
            if i+split >= len(nums):
                return -1
            return i + split if nums[i+split] == target else -1


s = Solution()
print(s.search([9,8,7, 1,2,3,4,5,6], 5))
print(s.search(nums = [4,5,6,7,0,1,2], target = 0))
print(s.search(nums = [2,3,4,5,1], target = 1))