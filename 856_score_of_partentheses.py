class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in S:
            # print(stack)
            if i == "(":
                stack.append("(")
            if i == ")":
                if type(stack[-1]) == int:  # (n    <- ')'
                    top = 2*stack.pop()  # 2n
                    if not stack:
                        stack.append(top)
                        continue

                    if type(stack[-1]) == int:  # m2n
                        stack.append(top + stack.pop())
                    else:  # (2n
                        stack.pop()
                        stack.append(top)
                else:  # (
                    stack.pop()
                    if not stack:
                        stack.append(1)
                        continue
                    if type(stack[-1]) == int:  # n( <- ')'
                        stack.append(1 + stack.pop())
                    else:
                        stack.pop()  # (( <- ')'
                        stack.append(1)
        # print(stack)
        return stack[-1]


s = Solution()
print(s.scoreOfParentheses("()((()))"))