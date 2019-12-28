class Solution(object):

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        patific = list()
        patific_set = set()
        atlantic = list()
        atlantic_set = set()

        patific.append([1] * n)
        for i in xrange(m - 1):
            atlantic.append([0] * n)
            patific.append([0] * n)
        atlantic.append([1] * n)

        for i in xrange(m):
            patific[i][0] = 1
            atlantic[i][n - 1] = 1

        import Queue
        patific_queue = Queue.Queue()
        atlantic_queue = Queue.Queue()

        for j in xrange(m):
            for k in xrange(n):
                if patific[j][k] == 1:
                    patific_queue.put((j, k))
                if atlantic[j][k] == 1:
                    atlantic_queue.put((j, k))
        while(not patific_queue.empty()):
            (j, k) = patific_queue.get()
            if k != 0 and matrix[j][k] <= matrix[j][k - 1]:
                if patific[j][k - 1] == 0:
                    patific_queue.put((j, k - 1))
                patific[j][k - 1] = 1
            if j != 0 and matrix[j][k] <= matrix[j - 1][k]:
                if patific[j - 1][k] == 0:
                    patific_queue.put((j - 1, k))
                patific[j - 1][k] = 1
            if k != n - 1 and matrix[j][k] <= matrix[j][k + 1]:
                if patific[j][k + 1] == 0:
                    patific_queue.put((j, k + 1))
                patific[j][k + 1] = 1
            if j != m - 1 and matrix[j][k] <= matrix[j + 1][k]:
                if patific[j + 1][k] == 0:
                    patific_queue.put((j + 1, k))
                patific[j + 1][k] = 1

        while(not atlantic_queue.empty()):
            (j, k) = atlantic_queue.get()
            if k != 0 and matrix[j][k] <= matrix[j][k - 1]:
                if atlantic[j][k - 1] == 0:
                    atlantic_queue.put((j, k - 1))
                atlantic[j][k - 1] = 1
            if j != 0 and matrix[j][k] <= matrix[j - 1][k]:
                if atlantic[j - 1][k] == 0:
                    atlantic_queue.put((j - 1, k))
                atlantic[j - 1][k] = 1
            if k != n - 1 and matrix[j][k] <= matrix[j][k + 1]:
                if atlantic[j][k + 1] == 0:
                    atlantic_queue.put((j, k + 1))
                atlantic[j][k + 1] = 1
            if j != m - 1 and matrix[j][k] <= matrix[j + 1][k]:
                if atlantic[j + 1][k] == 0:
                    atlantic_queue.put((j + 1, k))
                atlantic[j + 1][k] = 1

        for j in xrange(m):
            for k in xrange(n):
                if patific[j][k] == 1:
                    patific_set.add((j, k))
                if atlantic[j][k] == 1:
                    atlantic_set.add((j, k))
        return list(map(lambda x: list(x), patific_set.intersection(atlantic_set)))


s = Solution()
matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]

print s.pacificAtlantic(matrix)
