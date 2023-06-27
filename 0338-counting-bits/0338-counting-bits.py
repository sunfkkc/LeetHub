class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        def cal(n):
            return (n & n-1)==0
        
        dp={}
        
        dp[0]=0
        res=[0]
        offset=1
        for i in range(1,n+1):
            
            if cal(i):
                offset=i
            
            dp[i]=1+dp[i-offset]
            res.append(dp[i])
            
        return res