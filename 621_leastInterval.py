from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        if not tasks:
            return 0
        c = Counter(tasks)
        m = max(c.values())
        if (m - 1) * n + m  >= len(tasks):
            count = -1
            for k in c.keys():
                if c[k] == m:
                    count += 1
            return (m-1) * n + m + count
        return len(tasks)


s = Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
print(s.leastInterval(tasks = ["A","A","A","B","B","B", "C","D","E","F","G","H"], n = 2))
