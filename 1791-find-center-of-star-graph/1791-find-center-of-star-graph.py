class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
        
        adj = defaultdict(int)
        
        for i in edges:
            u,v=i
            
            adj[u]+=1
            adj[v]+=1
            
        
        return max(adj, key=adj.get)