class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        I, J = i, j
        from collections import defaultdict
        if N == 0:
            return 0
        r = [[[0]*n for y in range(m)] for _ in range(N+1)]
        for i in range(len(r[0])):
            r[1][i][0] += 1
            r[1][i][len(r[0][0])-1] += 1
        for j in range(len(r[0][0])):
            r[1][0][j] += 1
            r[1][len(r[0])-1][j] += 1
        for t in range(2, N+1):
            for i in range(len(r[0])):
                for j in range(len(r[0][0])):
                    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= i+d[0] <= len(r[0]) - 1 and 0 <= j+d[1] <= len(r[0][0]) - 1:
                            r[t][i][j] += r[t-1][i+d[0]][j+d[1]]
        return sum([r[t][I][J] for t in range(N+1)]) % (10 ** 9 + 7)


s = Solution()
print(s.findPaths(2,2,2,0,0))