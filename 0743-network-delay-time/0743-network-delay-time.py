class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        t=[0]+[float('inf')]*n
        
        graph=defaultdict(list)
        q=deque([(0,k)])
        
        
        for u,v,w in times:
            graph[u].append((v,w))
            
        while q:
            
            time,node = q.popleft()
            
            if time<t[node]:
                t[node]=time
                
                for v,w in graph[node]:
                    q.append((time+w,v))
                    
        return max(t) if max(t) < float('inf') else -1