class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        
        res=[]
        def bt(arr,index):
            
            if sum(arr) == target:
                res.append(arr[:])
                return
            if sum(arr)>target:
                return
                
            
            for i,v in enumerate(candidates[index:]):
                arr.append(v)
                bt(arr,i+index)
                arr.pop()
        
        for i,v in enumerate(candidates):
            bt([v],i)
        return res
                