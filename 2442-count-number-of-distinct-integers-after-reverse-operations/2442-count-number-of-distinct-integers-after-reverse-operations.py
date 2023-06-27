class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=set(nums)
        
        for n in nums:
            a=''
            for c in range(len(str(n))-1,-1,-1):
                a+=str(n)[c]
            
            res.add(int(a))
        
        return len(res)