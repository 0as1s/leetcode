class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        stones_set = dict()
        for s in stones:
            stones_set[s] = set()
        stones_set[0].add(1)
        for s in stones:
            jumps = stones_set[s]
            for j in jumps:
                if j != 0 and s + j in stones_set:
                    stones_set[s + j].add(j - 1)
                    stones_set[s + j].add(j)
                    stones_set[s + j].add(j + 1)
        if len(stones_set[stones[-1]]) != 0:
            return True
        return False
