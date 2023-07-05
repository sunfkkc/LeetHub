class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.res=0
        visited=set()
        def bt(i):
            
            if i==n:
                self.res+=1
                return
            
            for j in range(n):
                
                if (j+1) % (i+1) ==0 or (i+1) % (j+1) ==0:
                    if j not in visited:
                        visited.add(j)
                        bt(i+1)
                        visited.remove(j)
                    
        bt(0)
        return self.res