class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sp,tp=0,0
        
        while sp<len(s) and tp<len(t):
            
            if s[sp] != t[tp]:
                tp+=1
            else:
                sp+=1
                tp+=1
        
        
        return True if sp==len(s) else False