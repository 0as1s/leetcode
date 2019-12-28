class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a and not b:
            return "0"
        if not a or not b:
            return a or b
        if len(a) <= len(b):
            a = "0" * (len(b) - len(a) + 1) + a
            b = "0" + b
        else:
            b = "0" * (len(a) - len(b) + 1) + b
            a = "0" + a
        c = 0
        r = []
        for i in range(len(a)-1, -1, -1):
            if a[i] == "0" and b[i] == "0":
                r.append(str(c))
                c = 0
            elif a[i] == "1" and b[i] == "1":
                r.append(str(c))
                c = 1
            else:
                if c == 0:
                    r.append("1")
                else:
                    r.append("0")
        s = "".join(reversed(r))
        return s if s[0] != "0" else s[1:]
