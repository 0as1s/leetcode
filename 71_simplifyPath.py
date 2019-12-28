class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split("/")
        stack = []
        for ll in l:
            if not ll or ll == ".":
                continue
            if ll == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(ll)
        return "/" + "/".join(stack)

s = Solution()
print(s.simplifyPath("/a//b////c/d//././/.."))
print(s.simplifyPath("/"))