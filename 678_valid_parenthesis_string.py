class Solution(object):
    def helper(self, stack, s, left, right):
        if self.left + left > self.right + (self.start - left):
            return False
        if self.right + right > self.left + (self.start - right):
            return False
        for i in range(len(s)):
            ss = s[i]    
            if ss == ")":
                if not stack:
                    return False
                else:
                    stack.pop()
            if ss == "(":
                stack.append(stack)
            if ss == "*":
                if not stack:
                    stack1 = list(stack)
                    stack2 = list(stack)
                    stack1.append("(")
                    return self.helper(stack1, s[i+1:], left+1, right) or self.helper(stack2, s[i+1:], left, right)
                else:
                    stack1 = list(stack)
                    stack2 = list(stack)
                    stack3 = list(stack)
                    stack1.append("(")
                    stack3.pop()
                    return self.helper(stack1, s[i+1:], left+1, right) or self.helper(stack2, s[i+1:], left, right) or self.helper(stack3, s[i+1:], left, right+1)
        return stack == []

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        c = Counter(s)
        self.left = c["("]
        self.right = c[")"]
        self.start = c["*"]
        if self.left > (self.right + self.start) or self.right > (self.left + self.start):
            return False
        return self.helper([], s, 0, 0)

""" def checkValidString(self, s: str) -> bool:
		def check_valid_string(stack, s, memo_dic):
			if (tuple(stack), s) in memo_dic:
				return memo_dic[(tuple(stack), s)]
			if not stack and s == '':
				memo_dic[(tuple(stack), s)] = True
			elif s == '':
				memo_dic[(tuple(stack), s)] = False

			else:
				new_string = s[1:]
				if s[0] == '(':
					stack.append('(')
					result = check_valid_string(stack, new_string, memo_dic)
					stack.pop()
					memo_dic[(tuple(stack), s)] = result
				elif s[0] == ')':
					try:
						stack.pop()
						result = check_valid_string(stack, new_string, memo_dic)
						stack.append('(')
						memo_dic[(tuple(stack), s)] = result
					except IndexError:
						memo_dic[(tuple(stack), s)] = False

				else:
					a = check_valid_string(stack, new_string, memo_dic)
					try:
						stack.pop()
						b = check_valid_string(stack, new_string, memo_dic)
						stack.append('(')
					except IndexError:
						b = False

					stack.append('(')
					c = check_valid_string(stack, new_string, memo_dic)
					stack.pop()
					memo_dic[(tuple(stack), s)] = any([a, b, c])
			return memo_dic[(tuple(stack), s)]

		memo_dic = dict()
		init_stack = deque()
		return check_valid_string(init_stack, s, memo_dic)
 """
