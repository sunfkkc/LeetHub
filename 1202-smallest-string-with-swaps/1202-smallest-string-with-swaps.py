class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        
        def dfs(i):
            
            visited[i]=True
            
            component.append(i)
            for j in adj_lst[i]:
                if not visited[j]:
                    dfs(j)
        
        n=len(s)
        
        adj_lst  = [ [] for _ in range(n)]
        
        for i,j in pairs:
            
            adj_lst[i].append(j)
            adj_lst[j].append(i)
            
        visited=[False for _ in range(n)]
        
        lst=list(s)
        
        for i in range(n):
            
            if not visited[i]:
                
                component=[]
                
                dfs(i)
                
                component.sort()
                
                chars = [lst[k] for k in component]
                
                chars.sort()
                
                for i in range(len(component)):
                    lst[component[i]]=chars[i]
                    
        return ''.join(lst)
                