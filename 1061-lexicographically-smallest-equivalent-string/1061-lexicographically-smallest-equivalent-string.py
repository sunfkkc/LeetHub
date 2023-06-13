class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        d=defaultdict(str)
        
        for i in set(s1+s2):
            d[i]=i
            
        def find(c):
            p=d[c]
            while p != d[p]:
                d[p]=d[d[p]]
                p=d[p]
            return p
            
        
        def union(c1,c2):
            p1,p2=find(c1),find(c2)
            
            while p1 != p2:
                
                if ord(p1) > ord(p2):
                    d[p1]=p2
                    p1=d[p1]
                else:
                    d[p2]=p1
                    p2=d[p2]
                
            
        
        
        for i in range(len(s1)):
            union(s1[i],s2[i])
            
        print(d)
            
        res=''
        
        for i in baseStr:
            if i not in d.keys():
                res += i
            else:
                res+=find(i)
        return res
            