class Solution(object):
    def tra(self, left, picked, start, n):
        if left == 0:
            self.result.add(tuple(picked))
        for i in range(start, n+1):
            picked.append(i)
            self.tra(left-1, picked, i+1, n)
            del(picked[-1])

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        if k == 0:
            return []
        self.result = set()
        self.tra(k, [], 1, n)
        return self.result

s = Solution()
