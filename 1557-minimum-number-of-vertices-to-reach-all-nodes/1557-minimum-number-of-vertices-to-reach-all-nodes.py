class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        l = [0 for i in range(n)]
        
        for i in edges:
            l[i[1]]+=1
        
        return [i for i,v in enumerate(l) if v==0]