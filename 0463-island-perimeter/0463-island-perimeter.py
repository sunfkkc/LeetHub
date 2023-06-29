class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=set()
        q=deque()
        
        for i in range(len(grid)):
            a=False
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    q.append((i,j))
                    visited.add((i,j))
                    a=True
                    break
            if a:
                break
        res=0
        while q:
            i,j=q.popleft()
            
            if i==0:
                res+=1
            if i==len(grid)-1:
                res+=1
            if j==0:
                res+=1
            if j==len(grid[0])-1:
                res+=1
                
            if i>0:
                if grid[i-1][j]==0:
                    res+=1
                
            if i<len(grid)-1:
                if grid[i+1][j]==0:
                    res+=1
                    
            if j>0:
                if grid[i][j-1]==0:
                    res+=1
                
            if j<len(grid[0])-1:
                if grid[i][j+1]==0:
                    res+=1
                    
            if i>0 and grid[i-1][j]==1 and (i-1,j) not in visited:
                q.append((i-1,j))
                visited.add((i-1,j))
            if i<len(grid)-1 and grid[i+1][j]==1 and (i+1,j) not in visited:
                q.append((i+1,j))
                visited.add((i+1,j))
            if j>0 and grid[i][j-1]==1 and (i,j-1) not in visited:
                q.append((i,j-1))
                visited.add((i,j-1))
            if j<len(grid[0])-1 and grid[i][j+1]==1 and (i,j+1) not in visited:
                q.append((i,j+1))
                visited.add((i,j+1))
            
        return res
            