class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        starts = [[0] * len(s) for _ in range(len(t))]
        starts[0][0] = 0 if t[0] == s[0] else -1
        for i in range(1, len(s)):
            if t[0] == s[i]:
                starts[0][i] = i
            else:
                starts[0][i] = starts[0][i-1]

        m = float("Inf")
        for i in range(1, len(t)):
            for j in range(i, len(s)):
                if j == i:
                    starts[i][j] = j if starts[i-1][j] != -1 and s[j] == t[i] else -1
                    continue
                if s[j] == t[i] and starts[i-1][j] != -1:
                    print(starts[i-1][j], starts[i][j-1])
                    starts[i][j] = max(starts[i-1][j], starts[i][j-1])
                else:
                    starts[i][j] = starts[i][j-1]
        s_,e = -1, -1
        for j in range(len(t)-1, len(s)):
            if s[j] != -1:
                if j - starts[len(t)-1][j] < m:
                    m = j - starts[len(t)-1][j]
                    s_ = starts[len(t)-1][j]
                    e = j
        print(starts)
        if m == float("Inf"):
            return ""
        return s[s_:e+1]

s = Solution()
s.minWindow(s = "ADOBECODEBANC", t = "ABC")