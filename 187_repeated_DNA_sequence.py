class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ss = set()
        r = set()
        for i in range(len(s)-10):
            if s[i:i+10] in ss:
                r.add(s[i:i+10])
            s.add(s[i:i+10])