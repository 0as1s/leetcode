class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        result = []
        queue = []
        from collections import defaultdict
        managee = defaultdict(list)
        for i, m in enumerate(manager):
            managee[m].append(i)
        del managee[-1]
        queue.append((headID, 0))
        queue.append(-1)
        print(managee)
        times = []
        while queue:
            m = queue[0]
            del queue[0]
            if m == -1 and not queue:
                break
            if m == -1:
                queue.append(-1)
                continue
            if m[0] not in managee:
                result.append(m[1])
                continue
            for mm in managee[m[0]]:
                queue.append((mm, m[1]+informTime[m[0]]))
        print(result)
        return max(result)


s = Solution()
print(s.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0, 0, 1, 0, 0, 0]))
