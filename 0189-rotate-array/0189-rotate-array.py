class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        def tp(arr,i,j):
            
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            return arr
                
        if k>len(nums):
            k%=len(nums)
        
        if k>0:
            
            tp(nums,0,len(nums)-1)
            
            tp(nums, 0, k-1)
            
            tp(nums, k, len(nums)-1)