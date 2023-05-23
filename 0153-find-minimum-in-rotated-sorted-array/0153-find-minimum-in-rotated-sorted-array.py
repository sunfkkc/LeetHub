class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        lo=0
        hi=len(nums)-1
        
        while nums[lo] > nums[hi]:
            mid=(lo+hi)//2
            if nums[mid] < nums[hi]:
                hi=mid
            else:
                lo=mid+1
        return nums[lo]