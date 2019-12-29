from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        if not ops:
            return 0
        for o in ops:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))

            # print(sum(stack))
        return sum(stack)


s = Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))