from collections import defaultdict


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        blue_edges_d = defaultdict(list)
        for s, e in blue_edges:
            blue_edges_d[s].append(e)
        red_edges_d = defaultdict(list)
        for s, e in red_edges:
            red_edges_d[s].append(e)

        # print(blue_edges_d)
        # print(red_edges_d)

        known_r = dict()
        known_b = dict()
        known_r[0] = 0
        known_b[0] = 0
        used = dict()
        used[0] = 0
        used_red = set()
        used_blue = set()
        used_red.add(0)
        used_blue.add(0)

        while True:
            if known_r:
                cur = min(known_r.keys(), key=lambda x: known_r[x])
                d = known_r[cur]
                used[cur] = min(used.get(cur, float("Inf")), d)
                used_red.add(cur)
                del (known_r[cur])
                for j in blue_edges_d[cur]:
                    if j not in used_blue and (j not in known_b.keys() or d + 1 < known_b[j]):
                        known_b[j] = d + 1
            if known_b:
                cur = min(known_b.keys(), key=lambda x: known_b[x])
                d = known_b[cur]
                used[cur] = min(used.get(cur, float("Inf")), d)
                used_blue.add(cur)
                del (known_b[cur])
                for j in red_edges_d[cur]:
                    if j not in used_red and (j not in known_r.keys() or d + 1 < known_r[j]):
                        known_r[j] = d + 1
            if not known_r and not known_b:
                break

        result = [-1] * n
        for k in used.keys():
            result[k] = used[k]
        result[0] = 0
        return result

s = Solution()
print(s.shortestAlternatingPaths(n = 3, red_edges = [[0,1],[1,2]], blue_edges = []))
print(s.shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]))
print(s.shortestAlternatingPaths(n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]))
print(s.shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]))
print(s.shortestAlternatingPaths(n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]))
print(s.shortestAlternatingPaths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]]))
