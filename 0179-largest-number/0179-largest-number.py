class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if sum(nums)==0:
            return "0"
        
        l=0
        for n in nums:
            if l < len(str(n)):
                l=len(str(n))
        
        nums.sort(key=lambda x: str(x)*l)
        
        res=''
        
        while nums:
            n = nums.pop()
            res+=str(n)
        return res