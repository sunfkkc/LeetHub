class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        
        adj=defaultdict(list)
        
        for i,j in roads:
            adj[i].append(j)
            adj[j].append(i)
        visited=set()
        
        self.fuel=0
        
        def dfs(i):
            
            visited.add(i)
            n=1.0
            for j in adj[i]:
                
                
                if j not in visited:
                    
                    n+= dfs(j)
                    
            
            if i==0:
                return 0
            self.fuel+=math.ceil(n/seats)
            
            return n
        
        dfs(0)
        return int(self.fuel)
            