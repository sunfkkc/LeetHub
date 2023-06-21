class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(r,c):
            
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!=1 :
                return 0
            
            grid[r][c]=0
            
            return (1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1)+dfs(r,c+1))
            
        
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res=max(dfs(i,j),res)
        return res