class StatusNode(object):
    def __init__(self, val):
        self.val = val
        self.end = False
        self.self_point = None
        self.next = None

def tra(s, start):
    if not start:
        return False
    if not s:
        return start.self_point and start.end or False
    if len(s) == 1 and (s[0] == start.val or start.val == "."):
        if start.end or (start.next and start.next.self_point and start.next.end):
            return True
        if not start.self_point:
            return False
    if not start.next and not start.self_point:
        return False
    if start.val != "." and s[0] != start.val:
        if start.self_point:
            return tra(s, start.next)
        return False
    if start.self_point:
        return (start.next and tra(s, start.next)) or tra(s[1:], start.self_point) or tra(s[1:], start.next)
    return tra(s[1:],start.next)


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        s = "$" + s
        p = '$' + p
        start = StatusNode("$")
        starts = []
        left = [1, ] * len(p)
        for i, c in enumerate(p):
            if c == "*":
                starts.append(i)
        for i, e in enumerate(starts):
            if i == len(starts) - 1:
                break
            if starts[i+1] - e == 2 and p[e-1] == p[starts[i+1]-1]:
                left[e] = 0
                left[e-1] = 0
        new_p = ""
        left[0] = 0
        for i, l in zip(p, left):
            if l:
                new_p += i
        p = new_p
        cur = start
        stack = []
        for c in p:
            if c == "*":
                cur.self_point = cur
            else:
                newNode = StatusNode(c)
                cur.next = newNode
                cur = newNode
                stack.append(cur)
        while stack:
            p = stack.pop()
            p.end = True
            if not p.self_point:
                break
        return tra(s, start)


s = Solution()
print(s.isMatch(s = "aa", p = "a"))
print(s.isMatch(s = "aa", p = "a*"))
print(s.isMatch(s = "ab", p = ".*"))
print(s.isMatch(s = "aab", p = "c*a*b"))
print(s.isMatch(s = "mississippi", p = "mis*is*p*."))
print(s.isMatch("aaa", "a*a"))
print(s.isMatch("a", "ab*"))
print(s.isMatch("bbbba",".*a*a"))
print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
print(s.isMatch("", ".*"))
print(s.isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))
print(s.isMatch("cbaacacaaccbaabcb", "c*b*b*.*ac*.*bc*a*"))