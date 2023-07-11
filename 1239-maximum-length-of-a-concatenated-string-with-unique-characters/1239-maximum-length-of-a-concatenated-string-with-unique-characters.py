class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        a=['']
        res=0
        
        for w in arr:
            
            for i in range(len(a)):
                
                c = w+a[i]
                
                if len(c)==len(set(c)):
                    a.append(c)
                    res=max(res,len(c))
                    
        return res