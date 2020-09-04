class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        B = list(range(len(A)))
        while True:
            if i >= len(A):
                return True
            if A[i] != B[i]:
                if i == len(A) - 1:
                    return False
                else:
                    if A[i+1] == B[i] and A[i] == B[i+1]:
                        i += 2
                    else:
                        return False
            else:
                i += 1