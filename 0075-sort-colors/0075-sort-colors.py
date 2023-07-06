class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l,r=0,len(nums)-1
        k=-1
        while l<=r:
            
            if nums[l]==2:
                tmp=nums[l]
                nums[l]=nums[r]
                nums[r]=tmp
                r-=1
            elif nums[l]==0:
                tmp=nums[k+1]
                nums[k+1]=0
                nums[l]=tmp
                k+=1
                l+=1
            else:
                l+=1
        return nums
                