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
        
        
        def dfs(n):
            if n==destination:
                return True
            
            if n not in visited:
                visited.add(n)
                
                for e in adj[n]:
                    res=dfs(e)
                    if res:
                        return True
                
                    
        return dfs(source)
        