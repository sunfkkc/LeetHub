class Solution(object):
    def kClosest(self, p, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        q=[]
        
        heapq.heapify(q)
        
        for x,y in p:
            
            heapq.heappush(q,[pow(x,2)+pow(y,2),x,y])
            
        res=[]
        for i in range(k):
            res.append(heapq.heappop(q)[1:])
            
        return res