class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited =set()
        
        self.res=0
        
        def bt(r,c,n):
            
            
            if r>=len(grid) or r<0 or c<0 or c>=len(grid[0]) or grid[r][c]==0 or (r,c) in visited:
                return
            
            n+=grid[r][c]
            self.res=max(self.res,n)
            
            visited.add((r,c))
            
            bt(r-1,c,n)
            bt(r+1,c,n)
            bt(r,c-1,n)
            bt(r,c+1,n)
            
            visited.remove((r,c))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                bt(i,j,0)
                
        return self.res