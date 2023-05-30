class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        adj_to=defaultdict(set)
        
        indegree=defaultdict(int)
        
        for i, row in enumerate(matrix):
            
            for j, cell in enumerate(row):
                
                if i< len(matrix)-1 and cell < matrix[i+1][j]:
                    adj_to[(i,j)].add((i+1,j))
                    indegree[(i+1,j)] +=1
                
                if j< len(row)-1 and cell < matrix[i][j+1]:
                    adj_to[(i,j)].add((i,j+1))
                    indegree[(i,j+1)]+=1
                
                if i>0 and cell< matrix[i-1][j]:
                    adj_to[(i,j)].add((i-1,j))
                    indegree[(i-1,j)]+=1
                    
                if j>0 and cell <matrix[i][j-1]:
                    adj_to[(i,j)].add((i,j-1))
                    indegree[(i,j-1)]+=1
        
        q = deque()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not indegree[(i,j)]:
                    q.append( ((i,j),1))
        
        res=0
        
        while q:
            cur,depth = q.popleft()
            
            res = max(res,depth)
            
            for adj in adj_to[cur]:
                indegree[adj] -=1
                if not indegree[adj]:
                    q.append((adj,depth+1))
                    
        return res
        
        