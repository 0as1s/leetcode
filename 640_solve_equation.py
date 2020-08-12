class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split("=")
        left_x = 0
        left_v = 0
        right_x = 0
        right_v = 0
        cur = 1
        stack = ""
        for s in left:
            if s == "+":
                if stack:
                    left_v += cur * int(stack)
                    stack = ""
                cur = 1
            elif s == "-":
                if stack:
                    left_v += cur * int(stack)
                    stack = ""
                cur = -1
            elif s == "x":
                if stack:
                    left_x += cur * int(stack)
                    stack = ""
                else:
                    left_x += cur
                cur = 1
            else:
                stack += s
        if stack:
            left_v += cur * int(stack)
            stack = ""
        cur = 1
        for s in right:
            if s == "+":
                if stack:
                    right_v += cur * int(stack)
                    stack = ""
                cur = 1
            elif s == "-":
                if stack:
                    right_v += cur * int(stack)
                    stack = ""
                cur = -1
            elif s == "x":
                if stack:
                    right_x += cur * int(stack)
                    stack = ""
                else:
                    right_x += cur
                cur = 1
            else:
                stack += s
        if stack:
            right_v += cur * int(stack)

        delta_x = left_x - right_x
        delta_v = left_v - right_v
        if delta_x == 0 and delta_v != 0:
            return "No solution"
        if delta_x == 0 and delta_v == 0:
            return "Infinite solutions"
        return "x=%d" % (-delta_v // delta_x)


s = Solution()
print(s.solveEquation("x+5-3+x=6+x-2"))
print(s.solveEquation("x=x"))
print(s.solveEquation("2x=x"))
print(s.solveEquation("2x+3x-6x=x+2"))
print(s.solveEquation("x=x+2"))
