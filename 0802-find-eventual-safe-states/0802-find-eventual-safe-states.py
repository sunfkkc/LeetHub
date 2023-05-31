class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        
        n=len(graph)
        
        indeg=[0]*n
        
        adj=[[] for i in range(n)]
        
        for i in range(n):
            
            indeg[i]=len(graph[i])
            
            for j in graph[i]:
                adj[j].append(i)
                
        q=deque()
        res=[]
        
        print(indeg)
        print(adj)
        
        for i in range(n):
            if indeg[i]==0:
                q.append(i)
        
        while q:
            
            u=q.popleft()
            
            res.append(u)
            
            for i in adj[u]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
                    
        return sorted(res)