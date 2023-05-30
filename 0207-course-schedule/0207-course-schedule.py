class Solution(object):
    def canFinish(self, n, pre):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj = defaultdict(list)
        
        degree=[0]*n
        
        for p,c in pre:
            degree[p]+=1
            adj[c].append(p)
        
        start=[i for i in range(len(degree)) if degree[i]==0]
        print(start)
        
        q=deque(start)
        
        while q:
            
            node=q.popleft()
            
            for c in adj[node]:
                
                degree[c]-=1
                
                if degree[c]==0:
                    q.append(c)
                    
        if not any(degree):
            return True
        return False