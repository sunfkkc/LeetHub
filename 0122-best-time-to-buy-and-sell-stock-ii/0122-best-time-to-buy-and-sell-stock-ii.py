class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        res=0
        
        for i in range(len(p)-1):
            
            
            if p[i] < p[i+1]:
                res+=p[i+1]-p[i]
                
        return res