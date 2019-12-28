class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        values = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        res = []
        left = list(range(1, n+1))
        while True:
            if k == 1:
                res.extend(left)
                break
            times = k // values[n-1]
            rest = k % values[n-1]
            if rest == 0:
                res.append(left[times-1])
                del(left[times-1])
                res.extend(reversed(left))
                break
            res.append(left[times])
            del(left[times])
            k = rest
            n -= 1
        return "".join(list(map(str, res)))


s = Solution()
print(s.getPermutation(4, 9))
print(s.getPermutation(3, 3))
print(s.getPermutation(3, 2))