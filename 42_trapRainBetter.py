class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = [0, ] * len(height)
        right = [0, ] * len(height)
        m = 0
        for i in range(len(height)):
            left[i] = m
            m = max(m, height[i])
        m = 0
        for i in range(len(height)-1, -1, -1):
            right[i] = m
            m = max(m, height[i])
        s = 0
        for i, h in enumerate(height):
            s += max(0, min(left[i], right[i]) - h)
        return s

s = Solution()
print(s.trap([1]))