def numDupDigitsAtMostN(self, N: int) -> int:
    def helper(s):
        non_repeat = 0
        carry = set()
        for i in range(len(s)-1):
            if s[i] in carry:
                return non_repeat
            carry.add(s[i])
            tem = int(s[i+1])
            for _ in range(int(s[i+1])):
                if str(_) in carry:
                      tem -= 1
            tem = max(tem, 0)
            for j in range(i+2, len(s)):
                tem *= (10-j)
            non_repeat += tem
        return non_repeat + (s[-1] not in carry)
    num = str(N)
    non_repeat = 0
	# compute non- repeat numbers smaller than a0000
    for l in range(1, len(num) + 1):
        if l == len(num):
             pre, i = int(num[0]) -1, 1
        else:
            pre, i = 9, 1
        while i < l:
            pre *= (10 - i)
            i += 1
        non_repeat += pre        
    return N - non_repeat - helper(num)
