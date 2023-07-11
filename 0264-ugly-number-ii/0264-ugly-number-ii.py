class Solution(object):
        
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[1]

        i2=0
        i3=0
        i5=0

        while len(ans)<n:

            num=min(ans[i2]*2, ans[i3]*3, ans[i5]*5)
            ans.append(num)

            if num==ans[i2]*2: 
                i2+=1
            if num==ans[i3]*3: 
                i3+=1
            if num==ans[i5]*5: 
                i5+=1
                
        return ans[n-1]