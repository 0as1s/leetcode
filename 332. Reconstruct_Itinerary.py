class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        from_nodes = defaultdict(lambda: [0, 0])
        degree = defaultdict(0)
        for k, v in tickets:
            from_nodes[v].append(v)
            degree[v][0] += 1
            degree[k][1] += 1
        keys = sorted(list(degree.keys()), key=lambda x: degree[x])
        cur = keys[0]
        r = [cur, ]
        

