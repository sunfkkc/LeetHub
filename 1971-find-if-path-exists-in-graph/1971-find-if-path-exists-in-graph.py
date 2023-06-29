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
        
        visited.add(source)
        
        def dfs(n):
            if n==destination:
                return True
            
            for i in adj[n]:
                
                if i not in visited:
                    
                    visited.add(i)
                    res=dfs(i)
                    if res:
                        return True
                    
        return dfs(source)
        