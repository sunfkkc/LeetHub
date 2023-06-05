class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        
        d ={ '2':['a','b','c'], '3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'] }
        
        res=[]
        def bt(i,letter):
            
            if i==len(digits):
                res.append(letter)
                return
            
            for c in d[digits[i]]:
                bt(i+1,letter+c)
        
        bt(0,'')
        
        return res