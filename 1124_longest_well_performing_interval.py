class Solution:
    def longestWPI(self, array: List[int]) -> int:
        delta=0
        ans=0
        d={}
        for i in range(len(array)):
            delta=delta+1 if array[i] >8 else delta-1
            if delta>0:
                ans=i+1
            else:
                if delta not in d:
                    d[delta]=i
                if delta-1 in d:
                    ans=max(ans,i-d[delta-1])
        return ans


# d to record previously calculated delta, e.g. d[delta] = i means array[0...i] has delta days tiring more than not tiring.
# therefore d[delta] = j and d[delta-1] = i means array[i...j] has a delta equals to 1
