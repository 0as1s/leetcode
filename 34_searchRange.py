class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]

        left = 0
        right = len(nums)
        found = False
        left_target = 0
        right_target = len(nums) - 1
        while left != right:
            m = (left + right) // 2
            if nums[m] == target:
                found = True
            if nums[m] == target and m != 0 and nums[m] > nums[m-1]:
                left_target = m
                break
            if nums[m] >= target:
                right = m
            else:
                left = m+1

        if not found:
            return [-1, -1]
        left = 0
        right = len(nums) -1
        while left != right:
            m = (left + right) // 2
            if m == len(nums)-1:
                break
            if nums[m] == target and nums[m] < nums[m+1]:
                right_target = m
                break
            if nums[m] <= target:
                left = m + 1
            else:
                right = m
        return left_target, right_target


s = Solution()
print(s.searchRange([1, 4], 4))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
# print(s.searchRange())