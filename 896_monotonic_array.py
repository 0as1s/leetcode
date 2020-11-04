class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in A[1:]:
            if i>A[0]:
                for j in range(1, len(A)):
                    if A[j] < A[j-1]:
                        return False
                return True
            if i<A[0]:
                for j in range(1, len(A)):
                    if A[j] > A[j-1]:
                        return False
                return True
        return True
