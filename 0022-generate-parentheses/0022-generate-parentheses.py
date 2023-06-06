class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res=[]
        def bt(c):
            
            if c.count("(") < c.count(")"):
                return
            if c.count("(") == c.count(")") == n:
                res.append(c)
                return
            
            if c.count("(") <n:
                bt(c+"(")
            bt(c+")")
        
        bt("(")
        return res
            
        