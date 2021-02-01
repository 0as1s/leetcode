class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict()
        for i in range(0, len(s) - minSize + 1):
            if set(s[i:i+minSize]) <= maxLetters:
                count[s[i:i+minSize]] += 1
        if not count:
            return False
        return max(count.values())
