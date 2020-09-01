class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        pre = S[0]
        left = 0
        right = 0
        res = []
        for i in range(len(S)):
            s = S[i]
            if pre != s:
                pre = s
                if right - left >= 2:
                    res.append([left, right])
                left = i
                right = i
            else:
                right = i
        if right - left >= 2:
            res.append([left, right])
        return res

s = Solution()
print(s.largeGroupPositions("bbbbaaaa"))