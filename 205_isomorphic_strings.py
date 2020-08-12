class Solution(object):

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        d = dict()
        for a, b in zip(s, t):
            if a in d.keys():
                if d[a] != b:
                    return False
            else:
                if b in d.values():
                    return False
                d[a] = b

        return True


s = Solution()
a = "ab"
b = "aa"
print s.isIsomorphic(a, b)
