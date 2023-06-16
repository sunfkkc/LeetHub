class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp={}
        
        def bt(i,t):
            
            if i==len(nums):
                
                return 1 if t == target else 0
            
            if (i,t) in dp:
                return dp[(i,t)]
            
            
            dp[(i,t)]=bt(i+1,t+nums[i]) + bt(i+1, t-nums[i])
            
            return dp[(i,t)]
        
        return bt(0,0)