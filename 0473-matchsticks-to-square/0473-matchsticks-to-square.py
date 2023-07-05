class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        
        l=sum(matchsticks)//4
        
        sides=[0]*4
        memo={}
        
        if sum(matchsticks) /4 !=l:
            return False
        
        
        matchsticks.sort(reverse=True)
        
        def bt(i):
            
            if i==len(matchsticks):
                return True
            if tuple(sides) in memo:
                return memo[tuple(sides)]
            for j in range(4):
                
                if sides[j]+matchsticks[i]<=l:
                    
                    sides[j]+=matchsticks[i]
                    
                    if bt(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            memo[tuple(sides)] = False
            return memo[tuple(sides)]
        return bt(0)
        