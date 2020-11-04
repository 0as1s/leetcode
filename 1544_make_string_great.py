class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = []
        for c in s:
            ss.append(c)
            if len(ss>=2) and abs(ord(ss[-1]) - ord(ss[-2])) == 32:
                ss.pop()
                ss.pop()
        return "".join(ss)
