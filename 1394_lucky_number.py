class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(arr)
        for k in sorted(c.keys(), lambda x=-x):
            if c[k] == k:
                return k
        return -1
