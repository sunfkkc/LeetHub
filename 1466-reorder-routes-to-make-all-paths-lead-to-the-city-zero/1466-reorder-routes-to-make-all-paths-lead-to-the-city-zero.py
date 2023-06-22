class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        edges=set((a,b) for a,b in connections)
        
        visited=set()
        
        self.res=0
        
        adj=defaultdict(list)
        
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
            
        
        def dfs(city):
            
            for nei in adj[city]:
                
                if nei in visited:
                    continue
                    
                if (nei,city) not in edges:
                    self.res+=1
                
                visited.add(nei)
                dfs(nei)
        visited.add(0)
        dfs(0)
        return self.res

        