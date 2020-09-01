class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        store = {
            "a": 0, "b": 0, "c": 0
        }
        left = 0
        right = -1
        res = 0
        while True:
            if store["a"]>0 and store["b"]>0 and store["c"]>0:
                res += len(s) - right
                store[s[left]] -= 1
                left += 1
            else:
                right += 1
                if right == len(s):
                    return res
                store[s[right]] += 1
