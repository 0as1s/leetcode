class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for s in strs:
            t = tuple(sorted(s))
            if t not in d:
                d[t] = []
            d[t].append(s)
        return d.values()

s = Solution()
print(s.groupAnagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"]))