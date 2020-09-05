class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur:
                count += 1
            else:
                count -= 1
                if count == 0:
                    cur = nums[i]
                    count  = 1
        return cur
