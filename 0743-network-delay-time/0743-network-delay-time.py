class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int"""
        
        
        adj=defaultdict(list)
        
        dist=[float('inf')]*(n+1)
        dist[k]=0
        
        for a,b,c in times:
            adj[a].append((b,c))
            
        q=deque([(0,k)])
        
        while q:
            
            c,n=q.popleft()
            
            for node,cost in adj[n]:
                
                if dist[node] > c+cost:
                    dist[node]=c+cost
                    q.append((c+cost,node))
                    
        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1