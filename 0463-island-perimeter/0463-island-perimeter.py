class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        visited=set()
        
        self.res=0
        
        def dfs(i,j):
            
            for ni,nj in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                
                if 0<=ni<=len(grid)-1 and 0<=nj<=len(grid[0])-1:
                    
                    if grid[ni][nj]==1:
                        
                        if (ni,nj) not in visited:
                            visited.add((ni,nj))
                            dfs(ni,nj)
                            
                    else:
                        self.res+=1
                else:
                    self.res+=1
        
        for i in range(len(grid)):
            a=False
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    visited.add((i,j))
                    dfs(i,j)
                    a=True
                    break
            if a:
                break
                
        
        return self.res