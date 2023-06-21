class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        d=defaultdict(int)
        for i in s:
            d[i]+=1
            
        
        arr=[]
        
        heapq.heapify(arr)
        for key in d:
            heapq.heappush(arr,[-d[key],key])
            
        res=''
        
        while arr:
            v,c=heapq.heappop(arr)
            res+=c*-v
        return res