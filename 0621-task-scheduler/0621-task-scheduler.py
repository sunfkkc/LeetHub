class Solution(object):
    def leastInterval(self, t, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = Counter(t)
        
        h = [-cnt for cnt in c.values()]
        heapq.heapify(h)
        
        time=0
        q=deque()
        
        while h or q:
            time +=1
            
            if h:
                cnt = 1+heapq.heappop(h)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(h,q.popleft()[0])
        return time