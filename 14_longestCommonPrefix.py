class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        l = min(map(len, strs))
        prefix = ""
        for i in range(l):
            c = strs[0][i]
            for s in strs:
                if c != s[i]:
                    return prefix
            prefix += c
        return prefix

s = Solution()
print(s.longestCommonPrefix( ["flower","flow","flight"]))
