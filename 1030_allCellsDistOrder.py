class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        cor = []
        for x in range(R):
            for y in range(C):
                cor.append((x, y))
        return sorted(cor, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))

