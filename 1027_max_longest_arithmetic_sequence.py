class Solution:
    """
    6 June 2020.
    DP - Bottom up.
    Look at the solution as to how it was done.    
    
    T: O(N^2). The use of the double for loops.
    S: O(N^2). The lengths of the dictionary in dp follows this order: 0, 1, 2, 3,...n. That's N^2.
    
    **The literal running time varies with LC. This same solution ran in 2.1ms and 1.1ms.**
    **The literal space time is consistent at like 150MB which is insanely high but beats 80%. **
    """
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # Minimum answer is always 2.
        if len(nums) < 2: 
            return len(A)  
        
        # The DP is a list of dictionaries. 
        # dp[i] is the dictionary for item i in nums
        # Each kv pair in dp[i] is delta:lengthOfSubsequence.
        n = len(nums)
        dp = [{} for i in range(n)]
        result = 2
        
        for i in range(1, n):
            for j in range(i):
                delta = nums[i] - nums[j]
                
                # If we've seen this delta with dp[j], then increase the length of the subseq by 1.
                # This is equivalent of dp[i] 'adding on' to the subsequence.
                if delta in dp[j]:
                    currentLength = dp[j].get(delta)
                    dp[i][delta] = currentLength + 1
                
                # Else, start a new subsequence with just dp[i] and dp[j].
                # Length is always two.
                else:
                    dp[i][delta] = 2
                
                # Update max.
                result = max(result, dp[i][delta])        
        return result
