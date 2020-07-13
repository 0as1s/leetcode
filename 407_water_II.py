class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n, m, ans = len(heightMap), len(heightMap[0]), 0
        v, heap = [[False] * m for _ in range(n)], []
        for i in range(n):
            for j in range(m):
                if i in (0, n - 1) or j in (0, m - 1):
                    v[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i, j))
        while heap:
            val, i, j = heapq.heappop(heap)
            for i_n, j_n in [[i, j + 1], [i + 1, j], [i, j - 1], [i - 1, j]]:
                if 0 <= i_n < n and 0 <= j_n < m and not v[i_n][j_n]:
                    ans, v[i_n][j_n] = ans + max(0, val - heightMap[i_n][j_n]), True
                    heapq.heappush(heap, (max(val, heightMap[i_n][j_n]), i_n, j_n))
        return ans


"""
        up_left = [[0] * len(heightMap[0]) for _ in range(len(heightMap))]
        for i in range(len(heightMap[0])):
            up_left[0][i] = heightMap[0][i]
        for i in range(len(heightMap)):
            up_left[i][0] = heightMap[i][0]
        for i in range(1, len(heightMap)):
            for j in range(1, len(heightMap[0])):
                up_left[i][j] = max(heightMap[i][j], min(up_left[i][j-1],up_left[i-1][j]))

        up_right = [[0] * len(heightMap[0]) for _ in range(len(heightMap))]
        for i in range(len(heightMap[0])):
            up_right[0][i] = heightMap[0][i]
        for i in range(len(heightMap)):
            up_right[i][-1] = heightMap[i][-1]
        for i in range(1, len(heightMap)):
            for j in range(len(heightMap[0])-2, 0, -1):
                up_right[i][j] = max(heightMap[i][j], min(up_right[i][j+1],up_right[i-1][j]))

        down_left = [[0] * len(heightMap[0]) for _ in range(len(heightMap))]
        for i in range(len(heightMap[0])):
            down_left[-1][i] = heightMap[-1][i]
        for i in range(len(heightMap)):
            down_left[i][0] = heightMap[i][0]
        for i in range(len(heightMap)-2, 0, -1):
            for j in range(1, len(heightMap[0])):
                down_left[i][j] = max(heightMap[i][j], min(down_left[i][j-1],down_left[i+1][j]))
        
        down_right = [[0] * len(heightMap[0]) for _ in range(len(heightMap))]
        for i in range(len(heightMap[0])):
            down_right[-1][i] = heightMap[-1][i]
        for i in range(len(heightMap)):
            down_right[i][-1] = heightMap[i][-1]
        for i in range(len(heightMap)-2, 0, -1):
            for j in range(len(heightMap[0])-2, 0, -1):
                down_right[i][j] = max(heightMap[i][j], min(down_right[i][j+1],down_right[i+1][j]))

        # print(np.array(up_left))
        # print(np.array(up_right))
        # print(np.array(down_left))
        # print(np.array(down_right))
        sum = 0
        for i in range(1, len(heightMap)-1):
            for j in range(1, len(heightMap[0])-1):
                up = min(up_left[i][j], up_right[i][j], down_left[i][j], down_right[i][j])
                sum += max(0, up - heightMap[i][j])
        return sum


"""
