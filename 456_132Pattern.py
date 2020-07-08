class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        stack = []
        min_ = [nums[0], ]
        for i in range(1, len(nums)):
            min_.append(min(min_[i-1], nums[i]))
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > min_[j]:
                while stack and stack[-1] <= min_[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
