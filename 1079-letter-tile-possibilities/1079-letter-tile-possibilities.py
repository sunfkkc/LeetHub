class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        
        self.res=0
        visited=set()
        
        d=defaultdict(int)
        
        for c in tiles:
            d[c]+=1
        
        def bt(s):
            
            if len(s)==len(tiles):
                return
            
            for j in set(tiles):
                b=s+j
                if b.count(j) <=d[j] and b not in visited:
                    self.res+=1
                    bt(b)
        bt('')
        return self.res