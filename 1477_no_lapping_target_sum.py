class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        if not arr or len(arr) == 1:
            return -1
        sum_arr = [arr[0]]
        for i in arr[1:]:
            sum_arr.append(sum_arr[-1]+i)
        l, r = 0, 1
        candidates = []
        for i, s in enumerate(sum_arr):
            if s == target:
                candidates.append((-1, i))
        if arr[0] == target:
            candidates.append((-1, 0))
        while True:
            if sum_arr[r] - sum_arr[l] == target:
                candidates.append((l, r))
                l += 1
                r += 1
            elif sum_arr[r] - sum_arr[l] > target:
                l += 1
            else:
                r += 1
            if r == len(sum_arr):
                break
        result = float("Inf")
        candidates = sorted(candidates, key = lambda x: x[1]-x[0])
        for i in range(len(candidates)):
            il, ir = candidates[i]
            if ir - il > result:
                break
            for j in range(i+1,len(candidates)):
                jl, jr = candidates[j]
                if (ir <= jl or jr <= il):
                    result = min(result, ir - il + jr - jl)
        if result == float("Inf"):
            return -1
        return result


s = Solution()
print(s.minSumOfLengths([3,2,2,4,3], 3))
print(s.minSumOfLengths([7,3,4,7], 7))
print(s.minSumOfLengths([4,3,2,6,2,3,4], 6))
print(s.minSumOfLengths([3,1,1,1,5,1,2,1], 3))
print(s.minSumOfLengths([2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 20))

"""
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # prefix sum to store the subarray sums for any i:j
        # basically find two arr st arr1[:i] sum = target and arr2[j:] sum =  target
        # and j >= i and the sum of lengths are minimum.
        
        pref = [0]
        dic = {0: -1}
        for i in range(len(arr)):
            pref.append(arr[i] + pref[-1])
            dic[pref[-1]] = i
            # dic: key sum from 0 to i, value i

        
        
        ans = 1000000
        
        one, two = 1000000 ,1000000
        for i in range(len(arr)):
            diff = pref[i+1] - target
            if diff in dic: # sum dic[diff] to i == target
                # found a subarray arr1 whose sum is target and get its legth
                # if found shorter array
                one = min(one, i - dic[diff])
                
            if one < 1000000 and pref[i+1] + target in dic:
                # somewhere like j, pref[j] - pref[i+1] == target
                # found a subarray arr2 whose sum is target.
                two = dic[pref[i+1] + target]
                # update the min
                ans = min(ans, one + two - i)
            
        return ans if ans < 1000000 else -1
"""
