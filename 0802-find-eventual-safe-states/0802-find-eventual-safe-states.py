class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        n=len(graph)
        
        indegree=[0]*n
        
        adj=defaultdict(list)
        
        for i in range(n):
            
            indegree[i]=len(graph[i])
            for j in graph[i]:
                
                adj[j].append(i)
                
            
        print(adj)
        print(indegree)
        
        q=deque()
        
        res=[]
        
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                
        while q:
            u=q.popleft()
            
            res.append(u)
            
            for i in adj[u]:
                indegree[i]-=1
                
                if indegree[i]==0:
                    q.append(i)
        return sorted(res)