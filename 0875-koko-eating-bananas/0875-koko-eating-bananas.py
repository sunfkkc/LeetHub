class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        
        
        if len(p)==1:
            
            return math.ceil(p[0]/h)
        
        l,r=0,max(p)
        
        def con(a):
            
            b=0
            for i in p:
                b+=math.ceil(i/a)
                
            return b<=h
        
        while l<r:
            
            m=(l+r)//2
            
            if con(m):
                r=m
            else:
                l=m+1
        return l