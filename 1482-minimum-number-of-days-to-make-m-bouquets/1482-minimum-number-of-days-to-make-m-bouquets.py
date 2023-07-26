class Solution(object):
    def minDays(self, b, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        
        def con(mid):
            c=0
            r=0
            for n in b:
                if mid>=n:
                    c+=1
                    if c>=k:
                        r+=1
                        c=0
                else:
                    if c>=k:
                        r+=1
                    c=0
            return r+c//k>=m
                    
            
        
        if m*k > len(b):
            return -1
        
        l=min(b)
        r=max(b)
        mid=0
        
        while l<r:
            
            mid=(l+r)//2
            
            if con(mid):
                r=mid
            else:
                l=mid+1
        return l