class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
        
        res=set()
        
        def bt(w):
            if len(w)==n:
                res.add(int(w))
                return
            
            l = int(w[-1])
            
            
            if l+k<10:
                bt(w+str(l+k))
                
            if l>=k:
                bt(w+str(l-k))
            
            
        for i in range(1,10):
            bt(str(i))
        return list(res)