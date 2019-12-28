class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romes = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        r = ""
        while num != 0:
            factor = num // ints[i]
            remain = num % ints[i]
            r = r + (factor * romes[i])
            i += 1
            num = remain
        return r

s = Solution()
print(s.intToRoman(1994))

