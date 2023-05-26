class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        countP={}
        window={}
        
        for c in p:
            countP[c]=countP.get(c,0)+1
        
        
        
        have,need=0,len(countP)
        
        l=0
        res=[]
        
        for r in range(len(s)):
            
            c=s[r]
            
            window[c]=window.get(c,0)+1
            
            if r-l+1 ==len(p):
                
                if window==countP:
                    res.append(l)
                
                window[s[l]] -=1
                if window[s[l]] ==0:
                    del window[s[l]]
                l+=1
        
        return res