class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        
        res=0
        
        visited=set()
        
        def dfs(i):
            
            visited.add(i)
            for j,v in enumerate(isConnected[i]):
                
                if j not in visited and v==1:
                    
                    dfs(j)
                    
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                res+=1
                
        return res