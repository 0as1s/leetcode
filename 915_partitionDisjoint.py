class Solution:

    def partitionDisjoint(self, A):
        tmp, pos, m = A[0], 0, A[0]
        for i in range(1,len(A)):
            m = max(m, A[i])
            if A[i] < tmp:
                pos = i
                tmp = m
        return pos+1

