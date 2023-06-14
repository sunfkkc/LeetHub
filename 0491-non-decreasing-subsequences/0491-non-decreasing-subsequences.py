class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res=set()
        
        def bt(i,seq):
            
            if i==len(nums):
                if len(seq) >1:
                    res.add(tuple(seq))
                return
            
            if not seq or seq[-1] <= nums[i]:
                seq.append(nums[i])
                bt(i+1,seq)
                seq.pop()
                
            bt(i+1,seq)
        
        bt(0,[])
        return res
            