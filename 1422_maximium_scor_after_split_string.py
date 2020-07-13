class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 1:
            return  0
        if len(s) == 2:
            if s == "01":
                return 2
            if s == "10":
                return 0
            return 1
        ones = [0] * len(s)
        ones[-1] = 1 if s[-1] == "1" else 0
        for i in range(len(s)-2, -1, -1):
            ones[i] = ones[i+1] + 1 if s[i] == "1" else ones[i+1]
        print(ones)
        zeros = 1 if s[0] == "0" else 0
        r = zeros + ones[1]
        for i in range(1, len(s)-1, 1):
            if s[i] == "0":
                zeros += 1
                r = max(zeros + ones[i],  r)
        return r

s = Solution()
print(s.maxScore("011101"))
print(s.maxScore("00111"))
print(s.maxScore("1111"))
