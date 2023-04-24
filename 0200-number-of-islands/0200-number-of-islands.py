class Solution(object):
        
        
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row,col = len(grid), len(grid[0])
        
        answer=0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    self.dfs(grid,r,c)
                    answer+=1
        return answer
        
    def dfs(self,grid,r,c):
        
        if( r<0 or c<0 or r>=len(grid) or c>= len(grid[0])): return
        
        if( grid[r][c] =="1"):
            grid[r][c]="0"
            self.dfs(grid,r+1,c)
            self.dfs(grid,r-1,c)
            self.dfs(grid,r,c-1)
            self.dfs(grid,r,c+1)
        
                    
                    
                    