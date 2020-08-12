from collections import defaultdict

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved = dict()
        for a,b in reservedSeats:
            if a not in reserved:
                reserved[a] = ["0"] * 10
            reserved[a][b-1] = "1"
        def get(i, pos):
            i = i >> pos
            return i % 2
        m = defaultdict(int)
        for i in range(1025):
            res = [0] * 10
            for j in range(10):
                res[9-j] = get(i, j)
            if res[1] == 0 and res[2] == 0 and res[3] == 0 and res[4] == 0:
                m[i] += 1
            if res[5] == 0 and res[6] == 0 and res[7] == 0 and res[8] == 0:
                m[i] += 1
            if m[i] == 0:
                if res[5] == 0 and res[6] == 0 and res[3] == 0 and res[4] == 0:
                    m[i] += 1

        left = n*2
        for v in reserved.values():
            left -= (2 - m[int("".join(v), 2)])
        return left

s = Solution()
print(s.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
print(s.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]]))
print(s.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]]))
