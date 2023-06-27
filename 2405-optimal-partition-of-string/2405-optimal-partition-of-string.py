class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res=0
        
        b=set()
        a=''
        for c in s:
            
            if c in b:
                
                a=c
                res+=1
                b=set(c)
                
            else:
                
                b.add(c)
                a+=c
        if b:
            res+=1
        return res