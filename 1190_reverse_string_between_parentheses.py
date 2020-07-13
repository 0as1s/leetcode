class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        stack = [s[0]]
        for ss in s[1:]:
            if ss == ")":
                current_str = stack.pop()
                if current_str != "(":
                    stack.pop()
                else:
                    continue

                if not stack:
                    stack.append(current_str[::-1])
                    continue 
                if stack[-1] != "(":
                    pre_str = stack.pop()
                    pre_str += current_str[::-1]
                    stack.append(pre_str)
                else:
                    stack.append(current_str[::-1])
            elif ss == "(":
                stack.append("(")
            else:
                if stack[-1] != "(":
                    stack[-1] += ss
                else:
                    stack.append(ss)
        if not stack:
            return ""
        return stack[-1]


s = Solution()
print(s.reverseParentheses("a(bcdefghijkl(mno)p)q"))
print(s.reverseParentheses("(abcd)"))
print(s.reverseParentheses("(u(love)i)"))
print(s.reverseParentheses("()"))
print(s.reverseParentheses(""))