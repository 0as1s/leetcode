class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        if not S:
            return None
        indexes = []
        for i, e in enumerate(S):
            if C == e:
                indexes.append(i)
        r = [0, ] * len(S)
        for i in range(len(indexes)):
            cur = indexes[i]
            start = 0
            end = len(S)
            if i != 0:
                pre = indexes[i-1]
                start = cur - (cur - pre) // 2
            if i != len(indexes) - 1:
                next_ = indexes[i+1]
                end = cur + (next_ - cur) // 2 + 1
            for j in range(start, end):
                r[j] = j - cur if j > cur else cur - j
        return r


s = Solution()
print(s.shortestToChar("loveleetcode", "e"))