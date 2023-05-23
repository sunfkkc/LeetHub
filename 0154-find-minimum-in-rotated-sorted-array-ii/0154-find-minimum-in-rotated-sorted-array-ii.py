class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        
        lo=0
        hi=len(nums)-1
        
        while lo<hi:
            mid=(lo+hi)//2
            
            if nums[lo]==nums[mid]==nums[hi]:
                lo+=1
                hi-=1
            elif nums[mid]<=nums[hi]:
                hi=mid
            else:
                lo=mid+1
        return nums[lo]