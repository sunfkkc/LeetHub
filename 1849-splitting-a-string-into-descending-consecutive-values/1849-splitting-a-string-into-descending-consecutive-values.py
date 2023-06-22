class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.res=False
        def bt(i,n):
            if i==len(s)-1:
                self.res=True
                return
            
            for j in range(i+1,len(s)):
                a=int(s[i+1:j+1])
                if n-a ==1:
                    print(n,a,j)
                    bt(j,a)
                    
        
        for i in range(len(s)-1):
            bt(i,int(s[:i+1]))
        return self.res