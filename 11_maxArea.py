class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) in (0, 1):
            return 0
        l = 0
        r = len(height) - 1
        m = 0
        while l != r:
            m = max((r - l) * min(height[l], height[r]), m)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m


s = Solution()
print(s.maxArea([2,3,10,5,7,8,9]))
