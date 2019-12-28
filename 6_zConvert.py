class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        new_s = [["", ] * len(s) for _ in  range(numRows)]
        next_ = {
            1: (-1, 0), 0: (1, 1)
        }
        ss = 0
        cur = (0, 0)
        for c in s:
            new_s[cur[0]][cur[1]] = c
            n = (cur[0] + next_[ss][0], cur[1] + next_[ss][1])
            if not 0 <= n[0] < numRows:
                ss = 1 ^ ss
                n = (cur[0] + next_[ss][0], cur[1] + next_[ss][1])
            cur = n
        r = ""
        for i in new_s:
            for j in i:
                if j:
                    r += j
        return r

s = Solution()
print(s.convert(s = "LEETCODEISHIRING", numRows = 3))

