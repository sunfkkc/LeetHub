class Solution(object):
    def shipWithinDays(self, w, d):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        def con(m):
            a=0
            
            _d=0
            l,r=0,len(w)-1
            while l<=r:
                
                if a+w[l] <=m:
                    a+=w[l]
                else:
                    a=w[l]
                    _d+=1
                l+=1
            return _d <= d if a ==0 else _d+1 <=d
                
        
        l,r=max(w),sum(w)
        
        while l<r:
            
            mid=(l+r)//2
            
            if con(mid):
                r=mid
            else:
                l=mid+1
        return l