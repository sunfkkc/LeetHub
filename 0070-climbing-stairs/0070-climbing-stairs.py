class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp={}
        
        def bt(t):
            
            if t>n:
                return 0
            
            if t==n:
                return 1
            
            if t in dp:
                return dp[t]
            
            dp[t] = bt(t+1) + bt(t+2)
            
            return dp[t]
        
        return bt(0)