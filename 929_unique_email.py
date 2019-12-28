class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        r = set()
        for e in emails:
            p1, p2 = e.split("@")
            if "+" in p1:
                p1 = p1[:p1.index("+")]
            if "." in p1:
                p1 = p1.replace(".", "")
            r.add(p1+"@"+p2)
            # emails[i] = p1 + "@" + p2
        return len(r)


s = Solution()
print(s.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]))


