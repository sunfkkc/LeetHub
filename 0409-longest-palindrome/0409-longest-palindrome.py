class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d=defaultdict(int)
        
        for c in s:
            d[c]+=1
            
        res=0
        m=0
        
        for i in d:
            if d[i] %2 ==0:
                res+=d[i]
            else:
                if d[i]==1:
                    m=1
                else:
                    res+=d[i]-1
                    m=1
        return res+m