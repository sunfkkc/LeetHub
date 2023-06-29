class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        adj=defaultdict(list)
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        visited=set()
        
        q=deque([source])
        visited.add(source)
        
        while q:
            a=q.popleft()
            if a==destination:
                return True
            
            for i in adj[a]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        
        return False