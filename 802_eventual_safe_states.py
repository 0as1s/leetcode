class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        from heapq import heapify
        from collections import defaultdict
        from queue import deque
        out = defaultdict(list)
        count = defaultdict(int)
        for i, v in enumerate(graph):
            count[i] = len(v)
            for e in v:
                out[e].append(i)
        left = deque()
        r = []
        for k, v in count.items():
            if v == 0:
                left.append(k)
        while left:
            k = left.popleft()
            r.append(k)
            for n in out[k]:
                count[n] -= 1
                if count[n] == 0:
                    left.append(n)
        return sorted(r)
