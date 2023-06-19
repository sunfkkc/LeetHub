class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        visited=set()
        def bfs(r,c):
            
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or (r,c) in visited or grid[r][c] != 1:
                return 0
            
            
            
            visited.add((r,c))
                
            
            return (1+bfs(r-1,c)+
            bfs(r+1,c)+
            bfs(r,c-1)+
            bfs(r,c+1))
            
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res=max( bfs(i,j),res)
            
        return res