class Solution(object):
    @lru_cache
    def helper(s,shift,base):
        return chr(base + (ord(s) - base + shift) % 26)

    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shifts[-1] = shifts[-1] % 26
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] %= 26
            shifts[i] += shifts[i+1]
            shifts[i] %= 26
        res = []
        base = ord('a')
        for i in range(len(S)):
            res.append(helper(S[i], shifts[i], base))
        return "".join(res)
