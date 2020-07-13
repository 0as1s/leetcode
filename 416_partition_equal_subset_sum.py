class Solution:
    
    def canPartition(self, nums: List[int]) -> bool:
        
        nums_sum = sum(nums)
        
        if nums_sum%2:
            return False
        
        target = nums_sum//2
        vals = len(nums)
        
        dp = [[0 for i in range(target+1)] for j in range(vals+1)]
        
        for i in range(target+1):
            dp[0][i] = 0
            
        for i in range(vals+1):
            dp[i][0] = 1
            
        dp[0][0] = 1
        
        for i in range(1, vals+1):
            
            for j in range(1, target+1):
                
                ## dp[i][j] -> j sum can be formed using first i elements
                
                if nums[i-1]>j:
                    dp[i][j] = dp[i-1][j]
                
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    
        
        return dp[vals][target]