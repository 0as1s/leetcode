class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
           储存从头开始的i个和从尾开始的j个可以组成的最长的回文子序列
        '''
        len_s = len(s)
        t = s[::-1]
        arr = [[0 for x in range(len_s + 1)] for y in range(len_s + 1)]
        for i in range(1, len_s+1):
            for j in range(1, len_s + 1):
                if s[i-1] == t[j-1]:
                    arr[i][j] = arr[i-1][j-1] + 1 # 注意这里，匹配到一次只加1，因为反过来匹配到自己的时候一定还会加1
                else:
                    arr[i][j] = max(arr[i-1][j-1], arr[i-1][j],arr[i][j-1])
        return arr[len_s][len_s]