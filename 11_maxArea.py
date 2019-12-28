class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 1:
            return 0
        m = -float("Inf")
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                m = max(min(height[i], height[j]) * (j-i), m)

        return m
        # i_1 = 0
        # i_2 = 1
        # max_ = min(height[0], height[1])
        # for i in range(2, len(height)):
        #     a_1 = (i-i_1) * min(height[i], height[i_1])
        #     a_2 = (i-i_2) * min(height[i], height[i_2])
        #     if a_1 > max_ or a_2 > max_:
        #         if a_1 > a_2:
        #             i_2 = i
        #             max_ = a_1
        #         else:
        #             i_1 = i
        #             max_ = a_2
        # return max_

s = Solution()
print(s.maxArea([2,3,10,5,7,8,9]))
