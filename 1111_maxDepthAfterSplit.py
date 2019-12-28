class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

        stack = [0, ]
        deps = []
        for s in seq:
            # print(s, stack, deps)
            if s == "(":
                deps.append(stack[-1]+1)
                stack.append(stack[-1]+1)
            else:
                dep = stack.pop()
                deps.append(dep)
        ans = []
        m = max(deps)
        for i in deps:
            if i <= m // 2:
                ans.append(0)
            else:
                ans.append(1)
        return ans


s = Solution()
print(s.maxDepthAfterSplit("((()())(()())(()())(()())(()()))"))
# print(s.maxDepthAfterSplit("()(())()"))
# print(s.maxDepthAfterSplit("()(())()"))

