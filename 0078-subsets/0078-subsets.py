class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        res=[]
        
        
        
        def bt(i,letter):
            
            if i==len(nums):
                
                res.append(list(letter))
                return
            letter.append(nums[i])
            
            bt(i+1,letter)
            letter.pop()
            bt(i+1,letter)
        
        
        bt(0,[])
        return res
            