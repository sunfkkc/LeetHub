class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(i):
            c.add(i)
            
            for child in adj[i]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
        
        ans=0
        visited=set()
        
        for i in range(n):
            if i not in visited:
                c=set()
                visited.add(i)
                dfs(i)
                
                if all( len( adj[node]) == len(c)-1 for node in c):
                    ans+=1
        return ans
                
                