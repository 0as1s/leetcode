"length of longest substring with no same characters"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        m = 0
        start = 0
        d = {}
        for i, c in enumerate(s):
            if c in d and d[c] >= start:
                l = i - start
                m = max(m, l)
                start = d[c] + 1
            d[c] = i
        return max(m, len(s) - start)

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("12345"))
print(s.lengthOfLongestSubstring("dvdf"))