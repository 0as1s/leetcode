class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name or not typed:
            return False
        if len(typed) < len(name):
            return False
        s1 = []
        s2 = []
        pre = name[0]
        count = 1
        for s in name[1:]:
            if s == pre:
                count+=1
            else:
                s1.append((pre, count))
                pre = s
                count = 0
        pre = typed[0]
        count = 1
        for s in typed[1:]:
            if s == pre:
                count += 1
            else:
                s2.append((pre, count))
                pre = s
                count = 0
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i][0] != s2[i][0] or s1[i][1] > s2[i][1]:
                return False
        return True


s = Solution()
print(s.isLongPressedName(name = "laiden", typed = "laiden"))