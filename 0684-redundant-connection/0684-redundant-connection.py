class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        
        par=[i for i in range(len(edges)+1)]
        rank=[1] * (len(edges)+1)
        
        
        def find(n):
            if par[n]==n: return n
            par[n]=find(par[n])
            return par[n]
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p2]
            return True
                
        for n1,n2 in edges:
        
            if not union(n1,n2):
                return [n1,n2]