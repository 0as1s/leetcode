class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        next = [0, ] * len(needle)
        next[0] = -1
        j = -1
        for i in range(0, len(needle)-1):
            while True:
                if j == -1 or needle[i] == needle[j]:
                    # 在某一个时刻needle[i] == needle[j]
                    # 由于next数组的性质，[0..next[j]) 是 [0..j)后缀, 对于相等的needle[i]和needle[j]是一样的
                    # 因此不断的j=next[j]，然后判断needle[i] == needle[j]就可以找到使得对i成立的j，[0..j]是[0..i]的后缀
                    # 确定是后缀之后，i+1失配的时候，[0..j]是[0..i]的后缀，可以直接和j+1比
                    j += 1
                    i += 1
                    next[i] = j
                    break
                else:
                    j = next[j]
        # next[2] = 0
        i = 0
        j = 0
        print(next)
        while True:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
                if j == -1:
                    j += 1
                    i += 1
            if j == len(needle):
                return i-len(needle)
            if i == len(haystack):
                return -1


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("mississippi", "issip"))
print(s.strStr("mississippi", "abababca"))