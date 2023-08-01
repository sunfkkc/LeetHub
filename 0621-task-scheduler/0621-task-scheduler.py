class Solution(object):
    def leastInterval(self, t, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c= Counter(t)
        
        h=[-d for d in c.values()]
        
        heapq.heapify(h)
        
        q=deque()
        time=0
        while h or q:
            time+=1
            
            if h:
                a=heapq.heappop(h)+1
                if a !=0:
                    q.append([a,time+n])
                
            if q and q[0][1]==time:
                
                b=q.popleft()
                heapq.heappush(h,b[0])
        return time