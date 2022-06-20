# Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        dp = [0]*(n+1)
        
        dp.insert(0,0)
        dp.insert(1,1)
        dp.insert(2,2)
        
        
        for i in range(3, n+1):
            dp.insert(i, (dp[i-1] + dp[i-2]))
            
        return dp[n]        
