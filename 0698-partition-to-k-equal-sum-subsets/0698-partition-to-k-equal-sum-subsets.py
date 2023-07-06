class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        g=sum(nums)//k
        memo={}

        if g != sum(nums)/k:
            return False
        
        nums.sort(reverse=True)
        
        a=[0]*k
        
        def bt(i):
            
            if i==len(nums):
                return True
            if tuple(a) in memo:
                return memo[tuple(a)]
            for j in range(k):
                
                if a[j] + nums[i] <= g:
                    a[j]+=nums[i]
                    if bt(i+1):
                        return True
                    
                    a[j]-=nums[i]
            memo[tuple(a)] = False
            return memo[tuple(a)]
        return bt(0)