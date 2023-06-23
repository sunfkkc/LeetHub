class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        e=set(map(tuple,connections))
        
        adj=defaultdict(list)
        
        for a,b in connections:
            adj[a].append(b)
            adj[b].append(a)
            
        visited=set()
        self.res=0
        def dfs(city):
            
            if city in visited:
                return
            visited.add(city)
            for i in adj[city]:
                
                if (i,city) not in e and i not in visited:
                    
                    self.res+=1
                dfs(i)
        dfs(0)
        return self.res