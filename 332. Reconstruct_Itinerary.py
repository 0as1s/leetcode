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
        min_key = min([degree[x][1] - degree[x][0] for x in degree.keys()])
        keys = filter(lambda x: degree[x][1] - degree[x][0] == min_key, list(degree.keys()))
        cur = sorted(keys)[-1]
        
