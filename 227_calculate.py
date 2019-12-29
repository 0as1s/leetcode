class Solution(object):

    def pop_sigs(self, sigs, nums):
        # print(sigs)
        # print(nums)
        while sigs:
            n1 = nums.pop()
            n2 = nums.pop()
            sig = sigs.pop()
            if sig == "-":
                nums.append(n2 - n1)
            elif sig == "*":
                nums.append(n1 * n2)
            elif sig == "/":
                nums.append(n2 // n1)
            else:
                nums.append(n1 + n2)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(filter(lambda x: x != " ", s))
        nums = []
        sigs = []
        num = 0
        for i, c in enumerate(s):
            if '0' <= c <= '9':
                num = num * 10 + int(c)
                if i == len(s) - 1:
                    nums.append(num)
            elif c in "+-":
                nums.append(num)
                num = 0
                self.pop_sigs(sigs, nums)
                sigs.append(c)
                i += 1
            elif c in "*/":
                nums.append(num)
                num = 0
                if sigs and sigs[-1] in "*/":
                    n1 = nums.pop()
                    n2 = nums.pop()
                    sig = sigs.pop()
                    if sig == "*":
                        nums.append(n1*n2)
                    else:
                        nums.append(n2//n1)
                sigs.append(c)
                i += 1
        # print(nums)
        # print(sigs)
        if len(nums) >= 2:
            self.pop_sigs(sigs, nums)
        return nums[-1]


s = Solution()
print(s.calculate("3+2*22"))
print(s.calculate(" 3/2 "))
print(s.calculate(" 3+5 / 2 "))
print(s.calculate("1+1+1"))
print(s.calculate("42"))
print(s.calculate("1+7-7+3+3+6-3+1-8-2-6-1+8-0+0-2+0+10-6-9-9+0+6+4+2+7+1-4-6-6-0"))
print(s.calculate("1 + 1"))