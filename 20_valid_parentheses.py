class Solution(object):

    def isValid(self, s):
        pair = {')': '(', '}': '{', ']': '['}
        a = []
        for i in s:
            if not a and i in ")}]":
                return False
            if i in "({[":
                a.append(i)
            elif i in ")}]":
                if a[-1] == pair[i]:
                    a.pop()
                else:
                    return False
            else:
                return False
        return not a

t = "(])[]"
s = Solution()
print s.isValid(t)
