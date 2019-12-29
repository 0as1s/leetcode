class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        return min(len(set(candies)), len(candies) // 2)


s = Solution()
print(s.distributeCandies([1, 1, 2, 3]))