class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        left = []
        for x in arr:
            if x < 0:
                left.append(-((-x) % k))
            else:
                left.append(x % k)
        from collections import Counter
        c = Counter(left)
        for key in c:
            if key == 0:
                if c[key] % 2 != 0:
                    return False
            elif key < 0:
                s1 = c.get(-key, 0)
                s2 = c.get(-k-key, 0)
                if s1+s2<c[key]:
                    return False
            else:
                s1 = c.get(-key, 0)
                s2 = c.get(k-key, 0)
                if s1+s2<c[key]:
                    return False
        return True
