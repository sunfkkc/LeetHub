class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        self.res=[]
        
        self.s1=set()
        self.s2=set()
        self.s3=set()
        
        def createRow(c):
            result=['.']*n
            result[c]='Q'
            return ''.join(result)
        
        def bt(r,c,b):
            
            if r==n or c==n:
                return
            
            if c in self.s1:
                return
            if r-c in self.s2:
                return
            if r+c in self.s3:
                return
            
            line=createRow(c)
            b.append(line)
            
            if len(b) ==n:
                self.res.append(list(b))
                b.pop()
                return
            
            self.s1.add(c)
            self.s2.add(r-c)
            self.s3.add(r+c)
            
            for i in range(n):
                bt(r+1,i,b)
                
            self.s1.remove(c)
            self.s2.remove(r-c)
            self.s3.remove(r+c)
            b.pop()
            
        for i in range(n):
            bt(0,i,[])
        return self.res
            
        
        
            
    