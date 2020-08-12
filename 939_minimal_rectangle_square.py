
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        total = dict()
        x = defaultdict(list)
        y = defaultdict(list)
        
        for i, j in points:
            x[i].append(j)
            y[j].append(i)
            total[(i, j)] = 1

        for k in x:
            x[k] = sorted(x[k])
        for k in y:
            y[k] = sorted(y[k])
        # print(x)
        # print(y)
        # print(total.keys())
        min_area = float("Inf")
        for r in sorted(x.keys()):
            row = x[r]
            for i in range(len(row)):
                for j in range(i+1, len(row)):
                    if row[j] - row[i] > min_area:
                        break
                    for k in y[row[i]]:
                        if (row[j] - row[i]) * (k - r) > min_area:
                            break
                        if k <= r:
                            continue
                        #print((k, row[j]) == (3, 3))
                        if (k, row[j]) in total.keys():
                            # print(row[j], row[i])
                            min_area = min(min_area, (row[j] - row[i]) * (k - r))
                            break
        # print(min_area)
        return min_area if min_area != float("Inf") else 0


s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))