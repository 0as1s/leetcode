class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a_str = bin(a)[2:]
        b_str = bin(b)[2:]
        if len(a_str) < len(b_str):
            a_str = ("0" * (len(b_str) - len(a_str))) + a_str
        else:
            b_str = ("0" * (len(a_str) - len(b_str))) + b_str

        c = 0
        res = []
        #print(a_str)
        #print(b_str)
        for x, y in zip(reversed(a_str), reversed(b_str)):
            if c == 0:
                if (x, y) in [("1", "0"), ("0", "1")]:
                    res.append("1")
                elif (x, y) == ("1", "1"):
                    res.append("0")
                    c = 1
                else:
                    res.append("0")
            if c == 1:
                if (x, y) in [("1", "0"), ("0", "1")]:
                    res.append("0")
                    c = 1
                elif (x, y) == ("1", "1"):
                    res.append("1")
                    c = 1
                else:
                    res.append("1")
                    c = 0
        if c == 1:
            res.append("1")
        return int("".join(res)[::-1], 2)

s = Solution()
print(s.getSum(1, 2))