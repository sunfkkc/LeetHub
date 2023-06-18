class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        dp={}
        
        def dfs(i,t):
            if t==amount:    
                return 1
            if t>amount:
                return 0
            
            if i==len(coins):
                return 0
            
            if (i,t) in dp:
                return dp[(i,t)]
            
            dp[(i,t)] = dfs(i,t+coins[i]) + dfs(i+1,t)
            return dp[(i,t)]
                
        return dfs(0,0)
            
