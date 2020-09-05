class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        prefered_by = defaultdict(dict)
        for i, p in enumerate(preferences):
            for j, pp in enumerate(p):
                prefered_by[pp][i] = j
        pairs_d = dict()
        for x, y in pairs:
            pairs_d[x] = y
            pairs_d[y] = x
        count = 0
        for x in range(n):
            y = pairs_d[x]
            for u in range(n):
                if u == x:
                    continue
                v = pairs_d[u]
                if prefered_by[y][x] > prefered_by[u][x] and prefered_by[v][u] > prefered_by[x][u]:
                    count += 1
                    break
        return count


s = Solution()
print(s.unhappyFriends(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]))
print(s.unhappyFriends(2, [[1], [0]],  [[1, 0]]))
print(s.unhappyFriends(4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]]))
