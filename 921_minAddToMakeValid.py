class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = 0
        stack = []
        for c in S:
            if c == "(":
                stack.append(c)
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    count += 1
        count += len(stack)
        return count

s = Solution()
print(s.minAddToMakeValid("()"))