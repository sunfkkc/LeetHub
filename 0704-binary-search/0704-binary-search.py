class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        l=0
        r=len(nums)-1
        
        
        while l<=r:
            mid=(r+l)//2
            
            if nums[mid]<target:
                l=mid+1
                
            elif nums[mid]>target:
                r=mid-1
            else:
                return mid
                
                
        return -1