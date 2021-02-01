class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter, defaultdict
        r = 0
        A = Counter(A)
        B = Counter(B)
        C = Counter(C)
        D = Counter(D)
        AB = defaultdict(int)
        CD = defaultdict(int)
        for i in A:
            for j in B:
                AB[i+j] += A[i]*B[j]
        for i in C:
            for j in D:
                CD[i+j] += C[i]*D[j]
        r = 0
        for i in AB:
            if -i in CD:
                r += AB[i] * CD[-i]

        return r
