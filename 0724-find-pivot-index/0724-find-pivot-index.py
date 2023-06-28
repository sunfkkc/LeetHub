class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s=sum(nums)
        k=0
        for i in range(len(nums)):
            if i!=0:
                k+=nums[i-1]
            
            if k==s-nums[i]-k:
                return i
            
        return -1
            
            