class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1l=len(word1)
        w2l=len(word2)
        dp=[[0 for j in range(w2l+1)] for i in range(w1l+1)]
        
        for i in range(1,w1l+1):
            dp[i][0]=i
        for i in range(1,w2l+1):
            dp[0][i]=i
        
        for i in range(1,w2l+1):
            for j in range(1,w1l+1):
                
                if word1[j-1]==word2[i-1]:
                    dp[j][i]=dp[j-1][i-1]
                else:
                    dp[j][i]=min(dp[j-1][i-1], dp[j-1][i], dp[j][i-1])+1
        
        return dp[w1l][w2l]