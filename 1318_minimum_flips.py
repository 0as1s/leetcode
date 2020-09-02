class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        a_str = bin(a)[2:]
        b_str = bin(b)[2:]
        c_str = bin(c)[2:]
        l = max([len(a_str), len(b_str), len(c_str)])
        a_str = "0" * (l-len(a_str)) + a_str
        b_str = "0" * (l-len(b_str)) + b_str
        c_str = "0" * (l-len(c_str)) + c_str

        count = 0
        for i in range(l):
            if c_str[i] == "0":
                if b_str[i] == "1":
                    count += 1
                if a_str[i] == "1":
                    count += 1
            if c_str[i] == "1":
                if a_str[i] == "1" or b_str[i] == "1":
                    continue
                count += 1
        return count
