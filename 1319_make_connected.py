from queue import deque
from collections import defaultdict
class Solution(object):
    def bfs(self, n, neighbors, visited):
        visited.add(n)    
        q = deque()
        q.append(n)
        while q:
            cur = q.pop()
            for next in neighbors[q]:
                if next not in visited:
                    q.append(next)
                    visited.add(next)
        
    
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n-1:
            return -1
        neighbors = defaultdict(list)            
        visited = set()
        count = 0
        for c in connections:
            neighbors[c[0]].append(c[1])
            neighbors[c[1]].append(c[0])
        for i in range(n):
            if i not in visited:
                count += 1
                self.bfs(i, neighbors, visited)
        return count - 1
