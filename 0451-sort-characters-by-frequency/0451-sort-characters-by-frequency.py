class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        d=defaultdict(int)
        for i in s:
            d[i]+=1
            
        
        
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        
        res=''
        for i in d:
            for j in range(i[1]):
                res+=i[0]
        
        return res