class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        d=defaultdict(list)
        
        for i,j in edges:
            
            
            
            d[i].append(j)
            d[j].append(i)
             
        r=set(restricted)
        visited=set()
        
        q=deque([0])
        
        while q:
            
            n=q.popleft()
            
            
            visited.add(n)
            
            for k in d[n]:
                
                if k not in visited and k not in r:
                    
                    q.append(k)
                    
        return len(visited)