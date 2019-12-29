class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        # self.self_point = None
        self.end = False
        self.count = 0


class Solution(object):
    def tra(self, s, cur):
        # print(s, cur.val, cur.end)
        if not cur:
            return False
        if not s and cur.end:
            return True
        if not s:
            if cur.val == "*":
                return self.tra(s, cur.next)
            return False
        if len(s) < cur.count:
            return False
        if cur.val == "?":
            return self.tra(s[1:], cur.next)
        if cur.val == "*":
            return self.tra(s, cur.next) or self.tra(s[1:], cur)# or self.tra(s[1:], cur.next)
        if s[0] != cur.val:
            return False
        return self.tra(s[1:], cur.next)

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        if p[-1] not in "*?" and s and p[-1] != s[-1]:
            return False
        head = Node(None)
        cur = head
        l = len(p.replace("*", ""))
        for pp in p:
            new_node = Node(pp)
            if pp == "*":
                if cur.val == "*":
                    continue
            else:
                l -= 1
            new_node.count = l
            cur.next = new_node
            cur = cur.next
        new_node = Node(None)
        new_node.end = True
        cur.next = new_node
        return self.tra(s, head.next)


s = Solution()
print(s.isMatch("aaaaaaa", "aa"))
print(s.isMatch("cb", "?a"))
print(s.isMatch("cbads", "*"))
print(s.isMatch("adceb", "*a*b"))
print(s.isMatch("cdcb", "*c?b"))
print(s.isMatch("", "*"))
print(s.isMatch("ho", "ho**"))
print(s.isMatch("bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab", "b*b*ab**ba*b**b***bba"))