class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=[]
        
        c=s
        
        while c:
            
            for i,v in enumerate(c):
                
                s1=set(c[:i+1])
                s2=set(c[i+1:])
                
                if not s1.intersection(s2):
                    res.append(i+1)
                    c=c[i+1:]
                    break
                    
        return res