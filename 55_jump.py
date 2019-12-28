class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(n+i, m)
            if m >= len(nums) - 1:
                return True
        return m >= len(nums) - 1


s = Solution()
print(s.canJump([2,3,1,1,4]))