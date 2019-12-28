class Solution(object):

    def repeatedSubstringPattern(self, s):
        l = len(s)
        if l == 1:
            return False
        if l == 2:
            return s[0] == s[1]
        for i in range(l):
            if s[i] != s[0]:
                break
        else:
            return True
        if s[:2] * (l / 2) == s:
            return True
        for i in range(3, l):
            if l % i:
                continue
            t = s[:i]
            for k in range(1, l / i):
                if not s[k * i:(k + 1) * i] == t:
                    break
            else:
                return True
        return False
s = Solution()
ss = "zzz"
print s.repeatedSubstringPattern(ss)
