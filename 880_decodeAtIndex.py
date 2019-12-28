class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        stack = []
        start = 0
        stack.append((S[start], "+", 1, 1))
        for i in range(start+1, len(S)):

            if "2" <= S[i] <= "9":
                if stack[-1][2] > K:
                    break
                stack.append((S[:i+1], "*", stack[-1][2] * int(S[i]), int(S[i])))
            else:
                stack.append((S[:i+1], "+", stack[-1][2] + 1, 1))
        # print(stack)
        while True:
            cur = stack.pop()
            # print("-----------")
            # print(K)
            # print(cur[2])
            # print("-----------")
            if cur[2] == K:
                for s in reversed(cur[0]):
                    if not ("2" <= s <= "9"):
                        return s
            if cur[1] == "*" and K > cur[2] // cur[-1]:
                K = K % (cur[2] // cur[-1])
                if K == 0:
                    for s in reversed(cur[0]):
                        if not ("2" <= s <= "9"):
                            return s
