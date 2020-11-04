class Solution(object):
    def helper(self, cur, left):
        flag1 = True
        flag2 = False
        for i in range(len(left)):
            if left[i] == 1:
                flag1 = False
                if (i+1) % (cur+1) == 0 or (cur+1) % (i+1) == 0:
                    flag2 = True
                    left[i] = 0
                    self.helper(cur+1, left)
                    left[i] = 1
        if flag1:
            self.count += 1
        if not flag2:
            return


    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        left = [1] * N
        self.count = 0
        self.helper(0, left)
        return self.count