class Solution(object):
    def helper(self, A, B, left):
        
        cur = []
        cur.append(A)
        cur.append(B)
        while left:
            ss = str(A+B)
            if A+B > 2 ** 31 -1:
                return None
            if not left.startswith(ss):
                return None
            A = B
            B = int(ss)
            cur.append(B)
            left = left[len(ss):]
        return cur
        
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        il = len(S)//2+1
        if S.startswith("0"):
            il = 2
        for i in range(1, il):
            jl = len(S) - i
            if S[i] == 0:
                jl = 2
            for j in range(1, jl):
                A = int(S[:i])
                B = int(S[i:i+j])
                left = S[i+j:]
                r = self.helper(A, B, left)
                if r:
                    return r
        return []
