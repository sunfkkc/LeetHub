class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        
        visited=set()
        
        def dfs(r,c):
            visited.add((r,c))
            
            grid[r][c]=0
            
            for x,y in [[r-1,c],[r+1,c],[r,c-1],[r,c+1] ]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1:
                    dfs(x,y)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]==1 and (i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1):
                    dfs(i,j)
        res=0        
        for i in grid:
            res+=sum(i)
        return res