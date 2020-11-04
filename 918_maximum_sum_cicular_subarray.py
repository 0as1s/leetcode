class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return max(A[0], A[1], A[0]+A[1])
        nm = -float("Inf")
        ncs = -float("Inf")
        for a in A:
            if ncs <= 0:
                ncs = a
            else:
                ncs += a
            nm = max(nm, ncs)
            # print(ncs)
        mm = float("Inf")
        mcs = float("Inf")
        ma = []
        for a in A:
            if mcs >= 0:
                mcs = a
                ma = [a, ]
            else:
                mcs += a
                ma.append(a)
                if a >= 0:
                    ma = []

            mm = min(mm, mcs)
        # print(ma)
        #print(nm)
        #print(sum(A) - mm)
        if len(ma) == len(A):
            return max(A)
        return max(nm, sum(A) - mm)
            
s = Solution()
print(s.maxSubarraySumCircular([1, -2, 3, -2]))
print(s.maxSubarraySumCircular([5,-3,5]))
print(s.maxSubarraySumCircular([3,-1,2,-1]))
print(s.maxSubarraySumCircular([3,-2,2,-3]))
print(s.maxSubarraySumCircular([-2,-3,-1]))
print(s.maxSubarraySumCircular([2,-2,2,7,8,0]))
print(s.maxSubarraySumCircular([-5, 3, 5]))
print(s.maxSubarraySumCircular([-4,-7,-1,-8,1,-5,9,3,8]))