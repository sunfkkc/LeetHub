class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        
        def bt(i,a,b):
            
            if i == len(num):
                return True
            
            for j in range(i,len(num)):
                c=num[i:j+1]
                if c[0]=='0' and len(c)>1:
                    continue
                if int(c) == a+b:
                    if bt(j+1,b,int(c)):
                        return True
                    
        for i in range(len(num)-2):
            a=num[:i+1]
            if a[0]=='0' and len(a) >1:
                continue
            for j in range(i+1,len(num)-1):
                b=num[i+1:j+1]
                if b[0]=='0' and len(b) >1:
                    continue
                if bt(j+1,int(a),int(b)):
                    return True
        return False