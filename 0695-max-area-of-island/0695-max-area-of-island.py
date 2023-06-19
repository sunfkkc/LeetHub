class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            area=0
            
            while q:
                r,c=q.popleft()
                grid[r][c]=0
                area+=1
                
                if r>0 and grid[r-1][c]==1:
                    grid[r - 1][c] = 0
                    q.append((r-1,c))
                
                if r<len(grid)-1 and grid[r+1][c]==1:
                    grid[r + 1][c] = 0
                    q.append((r+1,c))
                    
                if c>0 and grid[r][c-1]==1:
                    grid[r][c - 1] = 0
                    q.append((r,c-1))
                    
                if c<len(grid[0])-1 and grid[r][c+1]==1:
                    grid[r][c + 1] = 0
                    q.append((r,c+1))
            
            return area
        
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]==1:
                    res=max(bfs(i,j),res)
                    
        return res