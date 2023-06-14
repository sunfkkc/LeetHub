class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        part=[]
        
        def cal(w,l,r):
            while l<r:
                if w[l] != w[r]:
                    return False
                l,r=l+1,r-1
            return True
            
        
        def bt(i):
            
            if i==len(s):
                res.append(list(part))
                return
            
            for j in range(i,len(s)):
                if cal(s,i,j):
                    part.append(s[i:j+1])
                    bt(j+1)
                    part.pop()
                    
        bt(0)
        return res
        
        
        