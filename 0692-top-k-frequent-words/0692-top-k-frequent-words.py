class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d=defaultdict(int)
        
        for i in words:
            d[i]+=1
        
        q=[]
        heapq.heapify(q)
        
        for key in d:
            heapq.heappush(q,[-d[key],key])
            
        res=[]
        
        while q:
            v,c=heapq.heappop(q)
            
            res.append(c)
        return res[0:k]