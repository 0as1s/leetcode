class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s or len(s) == 1:
            return 0
        a = []
        pre = s[0]
        count = 1
        for e in s[1:]:
            if e != pre:
                a.append(count)
                count = 1
            else:
                count += 1
            pre = e
        a.append(count)
        count = 0
        for i in range(len(a)-1):
            count += min(a[i], a[i+1])
        return count

s = Solution()
print(s.countBinarySubstrings("10"))
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("10101"))