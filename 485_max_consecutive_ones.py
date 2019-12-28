class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        pre = None
        begin = None
        if all(nums):
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == 1 and (pre is None or pre == 0):
                begin = i
            if nums[i] == 0 and pre == 1:
                if i - begin > m:
                    m = i - begin
            pre = nums[i]
        if nums[-1] == 1:
            if m == 0:
                return 1
            if nums[-2] == 1:
                return max(m, len(nums) - begin)

        return m


s = Solution()
print s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
