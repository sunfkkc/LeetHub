class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        ht={}
        res=[]
        for i,c in enumerate(s):
            ht[c]=i
            
        i=0
        size=1
        end=-1
        while i<len(s):
            
            
            
            end=max(ht[s[i]],end)
            
            if i==end:
                res.append(size)
                size=0
            
            i+=1
            size+=1
        return res