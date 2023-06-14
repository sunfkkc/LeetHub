class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        
        res=[]
        
        def isInt(c):
            try:
                int(c)
                return True
            except:
                return False
        
        def bt(i,w):
            
            if i==len(s):
                res.append(w)
                return
        
            if isInt(s[i]):
                bt(i+1,w+s[i])
            
            else:
                bt(i+1, w+s[i].upper())
                bt(i+1, w+s[i].lower())
        bt(0,'')
            
        
        return res