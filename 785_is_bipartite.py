class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        A = set()
        B = set()
        visited = set()
        from queue import deque
        for i in range(len(graph)):
            if i in visited:
                continue
            q = deque()
            q.append((True, i))
            A.add(i)
            while q:
                turn, node = q.popleft()
                if node in A and node in B:
                    return False
                if node in visited:
                    continue
                edges = graph[node]
                for next_node in edges:
                    if turn:
                        B.add(next_node)
                    else:
                        A.add(next_node)
                    q.append((not turn, next_node))
                visited.add(node)
        return True
