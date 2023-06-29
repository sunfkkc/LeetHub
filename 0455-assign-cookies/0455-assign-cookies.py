class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        res=0
        g.sort()
        s.sort(reverse=True)
        while g and s:
            
            a=g.pop()
            
            for k in s:
                if k>=a:
                    res+=1
                    s.remove(k)
                    break
        return res