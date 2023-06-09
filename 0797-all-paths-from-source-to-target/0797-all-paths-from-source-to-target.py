class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        visited=set([0])
        res=[]
        
        def bt(i,path):
            
            
            if i==len(graph)-1:
                res.append(list(path))
                return
            
            for v in graph[i]:
                
                if v not in visited:
                    
                    path.append(v)
                    visited.add(v)
                    bt(v,path)
                    path.remove(v)
                    visited.remove(v)
                
            
        
        bt(0,[0])
        return res