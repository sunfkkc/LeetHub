class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
#         l=0
#         r=len(nums)-1
#         tarI=0
        
#         while l< r:
#             mid=(1+r)/2
            
#             if nums[mid] > target:
#                 r=mid-1
                
                
#             elif nums[mid] < target:
                
#                 l=mid+1
#                 tarI=l+1
                
#             else:
#                 return mid
            
            
#         return tarI
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
