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
                    a=True
                    break
            if a:
                break
        res=0
        while q:
            i,j=q.popleft()
            
            if (i,j) in visited:
                continue
            
            visited.add((i,j))
            
            for ni,nj in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
                if 0<=ni<=len(grid)-1 and 0<=nj<=len(grid[0])-1:
                    
                    if grid[ni][nj]==1:
                        q.append((ni,nj))
                    else:
                        res+=1
                else:
                    res+=1
                        
        return res  