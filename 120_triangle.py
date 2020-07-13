class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return  0
        if len(triangle) == 1:
            return triangle[0][0]

        below = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            above = triangle[i]
            temp = [min(above[j]+below[j], above[j]+below[j+1])for j in range(len(above))]
            below = temp
        return min(below)

s = Solution()
triangle = [
     [2],
]

print(s.minimumTotal(triangle))
