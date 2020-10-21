class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        g = [[float("Inf")] * N for _ in range(N)]
        print(g)
        for t in times:
            g[t[0]-1][t[1]-1] = t[2]
        for i in range(N):
            g[i][i] = 0
        visited = set([K-1,])
        while True:
            cur = g[K-1]
            min_i, min_d = 0, float("Inf")
            flag = True
            for i in range(len(cur)):
                
                if i not in visited and cur[i] < min_d:
                    min_d = cur[i]
                    min_i = i
                    flag = False
            if flag:
                print(visited)
                if len(visited) == len(cur):
                    return max(cur)
                else:
                    return -1
            visited.add(min_i)
            for i in range(len(cur)):
                cur[i] = min(cur[i], cur[min_i]+g[min_i][i])
