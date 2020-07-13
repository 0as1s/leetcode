class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) < 3:
            return 0
        A = sorted(A, key=lambda x: -x)
        for i in range(len(A) - 2):
            if A[i+2] + A[i+1] > A[i]:
                return A[i+2] + A[i+1] + A[i]
        return 0
