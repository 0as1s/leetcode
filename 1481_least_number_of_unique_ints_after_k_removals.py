class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict, Counter

        c = Counter(arr)
        occurs = defaultdict(int)
        left = len(c)
        for k_, v in c.items():
            occurs[v] += 1
        keys = sorted(list(occurs.keys()))
        for i in keys:
            if k > i * occurs[i]:
                left -= occurs[i]
                k -= i * occurs[i]
            else:
                left -= (k // i)
                return left
        return 0
