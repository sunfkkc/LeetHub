class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        d=defaultdict(lambda:bool(False))
        
        for j in jewels:
            d[j]=True
        res=0
        for s in stones:
            if d[s]:
                res+=1
        return res