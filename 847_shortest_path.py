from copy import deepcopy, copy
class Solution(object):
    def helper(self, node, visited_nodes, cur_len, cur):
        if cur_len >= self.m or cur_len >= 2*len(self.graph) or self.m == len(self.graph):
            return
        cur.add(node)
        if len(cur) == len(self.graph):
            self.m = min(self.m, cur_len)
            return
        for i in self.graph[node]:
            if i in visited_nodes[node] or i in cur:
                continue
            backup = set(visited_nodes[node])
            visited_nodes[node].add(i)
            self.helper(i, visited_nodes, cur_len+1, set(cur))
            visited_nodes[node] = backup
        for i in cur:
            if i in visited_nodes[node]:
                continue
            backup = set(visited_nodes[node])
            visited_nodes[node].add(i)
            self.helper(i, visited_nodes, cur_len+1, set(cur))
            visited_nodes[node] = backup


    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        self.m = float("Inf")
        self.graph = graph
        from collections import defaultdict
        for i in range(len(graph)):
            self.helper(i, defaultdict(set), 1, set())
        return self.m-1

#test = [[1,2,3,4,5,6,7,8], [0,2,3,4,5,6,7,8], [1,0,3,4,5,6,7,8], [1,2,0,4,5,6,7,8], [1,2,3,0,5,6,7,8], [1,2,3,4,0,6,7,8], [1,2,3,4,5,0,6,8], [1,2,3,4,5,6,0,8], [1,2,3,4,5,6,7,0]]
#test = [[1,2,3,4,5,6, 7],[0,2,3,4, 5, 6, 7],[1,0,3,4, 5, 6,7],[1,2,0,4, 5, 6,7], [1,2,3,0, 5, 6, 7], [1,2,3,4, 0, 6, 7], [1,2,3,4, 5, 0, 7], [1,2,3,4, 5, 6, 0]]
test = [[1,2,3],[0],[0],[0]]
s = Solution()

# test = [
#     [1,2,3,4,5,6,7,8,9,10,11],
#     [0,2,3,4,5,6,7,8,9,10,11],
#     [1,0,3,4,5,6,7,8,9,10,11],
#     [1,2,0,4,5,6,7,8,9,10,11],
#     [1,2,3,0,5,6,7,8,9,10,11],
#     [1,2,3,4,0,6,7,8,9,10,11],
#     [1,2,3,4,5,0,7,8,9,10,11],
#     [1,2,3,4,5,6,0,8,9,10,11],
#     [1,2,3,4,5,6,7,0,9,10,11],
#     [1,2,3,4,5,6,7,8,0,10,11],
#     [1,2,3,4,5,6,7,8,9,0,11],
#     [1,2,3,4,5,6,7,8,9,10,0],
# ]

test=[[2],[2,8],[0,1,3,4],[2],[2],[8,6],[5],[8],[1,5,7]]
print(s.shortestPathLength(test))