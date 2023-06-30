class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        a=prices[0]
        b=0
        
        for i in range(1,len(prices)):
            
            if prices[i]<a:
                a=prices[i]
                
            d=prices[i]-a
            
            if d>b:
                b=d
                
        return b