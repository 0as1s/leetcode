class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        if not s:
            return 0
        if s[0] not in "0123456789-+":
            return 0
        start = 0
        negative = False
        if s[start] in "+-":
            negative = s[start] == '-'
            start += 1
        if start == len(s):
            return 0
        while s[start] == "0":
            start += 1
            if start == len(s) or s[start] not in "0123456789":
                return 0
        cur = 0
        for c in s[start:]:
            if c not in "0123456789":
                return cur if not negative else -cur
            if not negative and (cur > 2 ** 31 // 10 or (cur == 2**31 // 10 and ord(c) - ord('0') > 7)):
                return 2 ** 31 - 1
            if negative and (cur > 2 ** 31 // 10 or (cur == 2**31 // 10 and ord(c) - ord('0') > 8)):
                return -2**31
            cur = cur * 10 + (ord(c) - ord('0'))
        return cur if not negative else -cur


s = Solution()
print(s.myAtoi(" -42"))