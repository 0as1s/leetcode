class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        r = []
        cur = ""
        last = ""
        while True:
            m = max(a,b,c)
            if m == 0:
                return "".join(r)
            if m == a:
                if not (cur == "a" and last == "a"):
                    last = r[-1] if r else ""
                    a -= 1
                    cur = "a"
                    r.append("a")
                else:
                    m = max(b, c)
                    if m == 0:
                        return "".join(r)
                    if m == b:
                        last = r[-1] if r else ""    
                        b -= 1    
                        cur = "b"
                        r.append("b")
                    else:
                        last = r[-1] if r else ""    
                        c -= 1    
                        cur = "c"
                        r.append("c")
            elif m == b:
                if not (cur == "b" and last == "b"):
                    b -= 1
                    cur = "b"
                    last = r[-1] if r else ""
                    r.append("b")
                else:
                    m = max(a, c)
                    if m == 0:
                        return "".join(r)
                    if m == a:
                        last = r[-1] if r else ""    
                        a -= 1    
                        cur = "a"
                        r.append("a")
                    else:
                        last = r[-1] if r else ""    
                        c -= 1    
                        cur = "c"
                        r.append("c")
            elif m == c:
                if not (cur == "c" and last == "c"):
                    c -= 1
                    cur = "c"
                    last = r[-1] if r else ""
                    r.append("c")
                else:
                    m = max(a, b)
                    if m == 0:
                        return "".join(r)
                    if m == a:
                        last = r[-1] if r else ""    
                        a -= 1    
                        cur = "a"
                        r.append("a")
                    else:
                        last = r[-1] if r else ""
                        b -= 1    
                        cur = "b"
                        r.append("b")

