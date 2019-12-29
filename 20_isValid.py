class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        part_map = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in ")}]":
                if not stack:
                    return False
                top = stack.pop()
                if top != part_map[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True



s = Solution()
print(s.isValid("{[]}"))
