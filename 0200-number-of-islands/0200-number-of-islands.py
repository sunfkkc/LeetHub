class Solution(object):
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        visited=set()
        
        res=0
        
        
        def dfs(r,c):
            
            if r>=0 and r<=len(grid)-1 and c>=0 and c<=len(grid[0])-1 and grid[r][c]=="1" and (r,c) not in visited:
                visited.add((r,c))
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
            
                
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c]=="1":
                    
                    dfs(r,c)
                    res+=1
        
        return res
                