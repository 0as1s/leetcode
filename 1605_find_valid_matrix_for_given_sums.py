from heapq import *

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        grid = [[0] * len(colSum) for _ in range(len(rowSum))]
        rowheap = [[rowSum[i], i] for i in range(len(rowheap))]
        heapify(rowheap)
        colheap = [[-colSum[i], i] for i in range(len(colheap))]
        heapify(colheap)

        while rowheap:
            r, i = heappop(rowheap)
            c, j = heappop(colheap)
            c = -c

            if c == r:
                grid[i][j] = c
            elif c>r:
                grid[i][j] = r
                heappush(colheap, [r-c,j])
            else:
                grid[i][j] = c
                heappush(rowheap, [r-c,i])
        return grid

    
