class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        dp = [[1]*i for i in range(1,numRows+1)]
        
        for i in range(2,numRows):
            for j in range(1,len(dp[i])-1):
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                
        return dp