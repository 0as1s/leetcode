class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        from collections import Counter
        min_A = float("Inf")
        max_A = -float("Inf")
        for i in A:
            if i < min_A:
                min_A = i
            if i > max_A:
                max_A = i
        c = Counter(A)
        spare = []
        for i in range(min_A+1, 2*max(max_A, len(A))):
            if i not in c:
                spare.append(i)
        spare = list(reversed(spare))
        repeated_keys = sorted(list(filter(lambda x: c[x] > 1, c.keys())))
        sum_ = 0
        for k in repeated_keys:
            while k > spare[-1]:
                spare.pop()
            for _ in range(c[k] - 1):
                sum_ += spare[-1] - k
                spare.pop()
        return sum_


s = Solution()
print(s.minIncrementForUnique([1,2,2]))
print(s.minIncrementForUnique([3,2,1,2,1,7]))
print(s.minIncrementForUnique([]))
print(s.minIncrementForUnique([0,2,2,]))
print(s.minIncrementForUnique([1,1,1,1,1,1,1,1,1,2]))
print(s.minIncrementForUnique([1,100]))