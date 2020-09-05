class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        min1 = min(A)
        max1 = max(A)
        mid = (min1+max1) / 2
        min2 = min([x for x in A if x >= mid])
        max2 = max([x for x in A if x < mid])

        return min(max(2*K - (max1-min1), 2*K-(min2 - max2)), max1-min1)