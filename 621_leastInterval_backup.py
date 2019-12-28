from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        if not tasks:
            return 0
        c = Counter(tasks)
        m = max(c.values())
        if n == 0:
            return len(tasks)
        if (m - 1) * n + m  >= len(tasks):
            count = -1
            for k in c.keys():
                if c[k] == m:
                    count += 1
            return (m-1) * n + m + count
        available = {}
        for k in c.keys():
            available[k] = 0
        t = 0
        i = 0

        while t < len(tasks):
            for k in sorted(c.keys(), key=lambda x: -c[x]):
                if available[k] <= i:
                    available[k] = i+n+1
                    i+=1
                    t+=1
                    c[k] -=1
                    if c[k] == 0:
                        del c[k]
                    break
            else:
                i += 1
        return i


s = Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
# print(s.leastInterval(tasks = ["A","A","A","B","B","B", "C","D","E","F","G","H"], n = 2))
