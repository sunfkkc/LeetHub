class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        
        res=[]
        part=[]
        
        def isPal(w):
            n=len(w)
            
            l,r=0,n-1
            
            while l<r:
                
                if w[l] != w[r]:
                    return False
                l,r=l+1,r-1
            return True
        
        def bt(i):
            
            
            if i==len(s):
                res.append(list(part))
                return
            
            for j in range(i,len(s)+1):
                
                if isPal(s[i:j+1]):
                    part.append(s[i:j+1])
                    bt(j+1)
                    part.pop()
        
        bt(0)
        return res